from models.base.Model import Model
class Locality(Model):
    def __init__(self, id = '', key ='', towns = [], state = '', municipality = '', city = '',createdOn = '', updatedOn = ''):
        Model.__init__(self, id, createdOn, updatedOn)
        self.key  = key
        self.towns = towns
        self.municipality = municipality
        self.city = city
        self.state = state
        pass
