#!/usr/bin/python3
"""Define HBnB console."""
import cmd
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        pass
        # Add implementation here

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id."""
        pass
        # Add implementation here

    # Implement other methods like do_destroy, do_all, do_count, and do_update

if __name__ == "__main__":
    HBNBCommand().cmdloop()
