#!/usr/bin/python3
"""
A module that defines a class called BaseModel
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Representing a class
    Defines attributes/methods for subclasses to inherit
    """

    def __init__(self):
        """ initialiaze class instance """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print human readable output """
        
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """ save updates of class instance attributes """

        updated_at = datetime.now()

    def to_dict(self):
        """ dictionary representation of our classe instance attributes 
        returns a dictionary containing all keys/value of __dict__
        of the instance:
            self.__dict__, a key __class__ must be added to the dictionary
            created_at, updated_at must be converted to string object
            in ISO format"""

        to_dictFormat = {}
        # adding a class key to identify class name
        # of the instance attribute

        to_dictFormat["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                to_dictFormat[key] = val.isoformat()
            else:
                to_dictFormat[key] = val
        return to_dictFormat
