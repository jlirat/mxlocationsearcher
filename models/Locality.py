
class Locality:
    def __init__(self, id = '', key ='', name = '', type_town = '', state = '', municipality = '', city = '',createdOn = '', updatedOn = ''):
        # Model.__init__(self, id, createdOn, updatedOn)
        self.key  = key
        self.name = name
        self.type_town = type_town
        self.municipality = municipality
        self.city = city
        self.state = state
        pass
