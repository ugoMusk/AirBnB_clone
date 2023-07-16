#!/usr/bin/python3
"""
File storage module
"""
import json
import os


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
        
        key = "{}.{}".format(type(obj).__name__, obj.id)
        # key = f'{type(obj).__name__}, {obj.id}'
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
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, "r", encoding="utf8") as file:
                obj_d = json.load(file)
                obj_d = {k: self.classes()[v["__class__"]](**v) for k, v in obj_d.items()}
                FileStorage.__objects = obj_d
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references"""

        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        return classes
