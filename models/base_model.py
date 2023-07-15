#!/usr/bin/python3
"""
A module that defines a class called BaseModel
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Representing a class
    """

    def __init__(self):
        """
        Initializing the BaseModel class
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        str representation
        """

        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """
        a method that updates the public instance
        attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of keys and values
        of self.__dict__, a key __class__ must be added to the
        dictionary created_at, updated_at must be converted to
        string object in ISO format
        """

        to_dictformat = {}
        # Adding a class key to identify class name
        # of the instance attribute

        to_dictformat["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                to_dictformat[key] = val.isoformat()
            else:
                to_dictformat[key] = val
        return to_dictformat
