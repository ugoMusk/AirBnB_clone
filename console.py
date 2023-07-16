#!/usr/bin/python3
"""
A module for the cmd console
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Representing the class """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """ Exists the program """

        return True

    def do_EOF(self, args):
        """ Exit the program """
        return True

    def emptyline(self):
        """ does not execute anything """
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = stoarage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """ Prints string representation of an instance """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the name and the id"""


if __name__ == "__main__":
    HBNBCommand().cmdloop()
