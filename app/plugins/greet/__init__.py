import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        logging.info("Greetings, Universe!")

        mylist_tuple = (1,2,3,4)
        mylist = [1,2,3,4]

        print("Greetings, Universe!")  # Make sure this prints the message

