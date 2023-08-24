#!/usr/bin/python3
"""
A module for the cmd console
"""
import cmd
from models.base_model import BaseModel, storage
import re


class HBNBCommand(cmd.Cmd):
    """ Representing the class """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Exists the program """

        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        """ does not execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.class_imports():
            print("** class doesn't exist **")
        else:
            b = storage.class_imports()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """ Prints string representation of an instance """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            cmd_args = line.split(" ")
            if cmd_args[0] not in storage.class_imports():
                print("** class doesn't exist **")
            elif len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                key = f'{cmd_args[0]}.{cmd_args[1]}'
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the name and the id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            cmd_args = line.split(" ")
            if cmd_args[0] not in storage.class_imports():
                print("** class doesn't exist **")
            elif len(cmd_args) < 2:
                print("** instance id missing **")
            else:
                key = f'{cmd_args[0]}.{cmd_args[0]}'
                if key is not storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        prints all string representation of class instances
        """
        if line != "":
            cmd_args = line.split(" ")
            if cmd_args[0] not in (storage.class_imports()):
                print("** class doesn't exist **")
            else:
                list_instances = []
                for key, value in (storage.class_imports()).items():
                    list_instances.append(value)
                print(list_instances)
        else:
            list_instances = []
            for key, value in storage.all().items():
                list_instances.append(key)
                print(list_instances)

    def do_update(self, line):
        """
        updates an instance based on class name
        and id by adding of removing attributes and
        saves to file
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            cmd_args = line.split(" ")
            if len(cmd_args) <= 3:

                if cmd_args[0] not in storage.class_imports():
                    print("** class doesn't exist **")
                elif len(cmd_args) < 2:
                    print("** instance id missing **")
                elif not isinstance(cmd_args[1], storage.all()[key]):
                    print("** no instance found  **")
                elif len(cmd_args) < 3:
                    print("** attribute name missing **")
                elif not isinstance(cmd_args[2], storage.all()[key]):
                    print("** value missing **")
                else:
                    pass
            else:
                pass
        key = {key: value for key, value in storage.__objects}
        if cmd_args[3] == key:
            pass
        else:
            storage.all()[key].save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
