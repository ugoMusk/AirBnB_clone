#!/usr/bin/python3
"""
A module for the cmd console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Representing the class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Exists the program """

        return True
    def do_EOF(self, arg):
        """ Exit the program """
        return True

    def emptyline(self):
        """ does not execute anything """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
