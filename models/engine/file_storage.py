#!/usr/bin/python3
"""
File storage module
"""
import json


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
            key = f'{type(obj).__name__}, {obj.id}'
            self.__objects[key] = obj

    def save(self):
        """
        save objects in json format to file
        """
        with open(self.__file_path, "w", encoding="utf8") as file:
            d = {key: v for key, v in self.__objects.items()}
            json.dump(d, file)

    def reload(self):
        """
        load json string from file to python object
        """
        try:
            with open(self.__file_path, "r", encoding="utf8") as file:
                obj_d = json.load(file)
        except FileNotFoundError:
            pass
