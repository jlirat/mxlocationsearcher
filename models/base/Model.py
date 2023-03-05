from abc import ABC
from datetime import datetime
from pytz import timezone

class Model(ABC):

    def __init__(self, id = 0, createdOn = '', updatedOn = ''):
        self.id = id
        if createdOn != '':
            self.createdOn = createdOn
        if updatedOn != '':
            self.updatedOn = updatedOn

    def as_dict(self):
        o = self.__dict__
        return o

    def to_dict(self):
        return self.this
    
    def from_dict(self, to):
        print(self.__dict__)
        for field in self.__dict__:
            print(field)
            if to is not None:
                if to.get(field):
                    self.__setattr__(field, to[field])
        pass


    def validate(self, params):
        for param in params:
            if param not in self.this and (param!='limit' and param!='orderBy' and param!='in'):
                params.pop(param)
        pass
