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
        #key = "{}.{}".format(type(obj).__name__, obj.id)
        key = f'{type(obj).__name__}.{obj.id}'
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
                obj_d = {k: self.class_imports()[v["__class__"]](**v) for k, v in obj_d.items()}
                FileStorage.__objects = obj_d
        except FileNotFoundError:
            pass

    def class_imports(self):
        """Returns a dictionary of valid classes and their references"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Review": Review,
                   "Place": Place}

        return classes

    def dot_cmds(self):
        """
        returns a list of class decorator methods
        """
        cmd_list = ['all', 'count',
                    'show','destroy',
                    'update']
        return cmd_list

    def types(self):
        """
        returns a dictionary object containing types of class attributes
        """
        attr_types ={
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }
        return attr_types
