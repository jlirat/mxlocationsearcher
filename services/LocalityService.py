from abc import ABC, abstractmethod
from unicodedata import normalize
import re
from bs4 import BeautifulSoup
from firebase_admin import credentials
from firebase_admin import firestore
from collections import namedtuple

from flask import jsonify, make_response
import requests
from models.Locality import Locality

def clean_string(cadena):
    cadena = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize( "NFD", cadena), 0, re.I
    ) 
    return cadena

class LocalityService:
    def getLocality(self, cp):
        print(cp)
        if len(cp)!=5:
            return {"message": str('Parameter postal code length is not valid'), "severity": "danger"}
            
        url = 'https://micodigopostal.org/buscarcp.php?buscar=' + cp
        
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.content
            soup = BeautifulSoup(datos, "html.parser")
            table = soup.find("table", { "id" : "dataTablesearch" })
            rows  = table.find_all('tr')
            loc = []
            key = cp
            
            for row in rows:
                # print('Fila:')
                cells = row.findAll("td")
                if len(cells)>0 and len(cells)==7:
                    newLoc = Locality()
                    newLoc.key = key
                    newLoc.name = cells[0].text.strip()
                    # loc.append(cells[0].text.strip())
                    newLoc.type_town = clean_string(cells[1].text.strip()).upper()
                    newLoc.municipality = clean_string(cells[3].text.strip()).upper()
                    newLoc.city = clean_string(cells[4].text.strip()).upper()
                    newLoc.state = clean_string(cells[6].text.strip()).upper()
                    loc.append(newLoc)

        return loc