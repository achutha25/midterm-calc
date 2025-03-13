import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info("Greetings, Universe!")

        numbers_tuple = (1, 2, 3, 4)
        numbers_list = [1, 2, 3, 4]

        print("Greetings, Universe!")

