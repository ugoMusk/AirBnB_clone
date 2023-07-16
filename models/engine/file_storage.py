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
        return FileStorage.__objects

    def new(self, obj):
        """
        creates new object of class
        """
        if obj:
            key = f'{type(obj).__name__}, {obj.id}'
            FileStorage.__objects[key] = obj

    def save(self):
        """
        save objects in json format to file
        """
        with open(FileStorage.__file_path, "w", encoding="utf8") as file:
            d = {key: v.to_dict() for key, v in FileStorage.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """
        load json string from file to python object
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf8") as file:
                obj_d = json.load(file)
        except FileNotFoundError:
            pass
