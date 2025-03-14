from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        print("Greetings, Universe!")  # Make sure this prints the message

