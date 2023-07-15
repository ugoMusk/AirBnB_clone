#!/usr/bin/python3
"""
File storage module
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Handles serialization and deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all objects of instance
        """
        return self.__objects

    def new(self, obj):
        """
        creates new object of class
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
