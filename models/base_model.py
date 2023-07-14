#!/usr/bin/python3

#import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines attributes/methods for subclasses to inherit
    """

    def __init__(self):
        """ initialiaze class instance """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print human readable output """
        return "[{}] {} {}".format(type(self).__name__, self.id, type(self).__dict__)
    
    def save(self):
        """ save updates of class instance attributes """
        self.created_at = datetime.now()
        return self.created_at

    def to_dict(self):
        """ dictionary representation of our classe instance attributes """

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return {"__class__" : getattr(self, "__class__"), "id" : getattr(self, "id"), "created_at" : getattr(self, "created_at"), "updated_at" : getattr(self, "updated_at")}
        
    
i_obj = BaseModel()
print(i_obj.to_dict())

