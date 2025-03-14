import pandas as pd
from abc import ABC, abstractmethod

# Initialize a DataFrame to keep track of calculation history
history_df = pd.DataFrame(columns=["Expression", "Result"])

# Function to add to the history
def add_to_history(expression, result):
    global history_df
    new_row = pd.DataFrame({"Expression": [expression], "Result": [result]})
    history_df = pd.concat([history_df, new_row], ignore_index=True)

def view_history():
    global history_df
    return history_df

# Abstract base Command class
class Command(ABC):
    @abstractmethod
    def execute(self, operand1, operand2):
        pass

# CommandHandler class to manage registered commands and their execution
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, operand1, operand2):
        try:
            self.commands[command_name].execute(operand1, operand2)
        except KeyError:
            print(f"No such command: {command_name}")


# Arithmetic Command Classes
class AddCommand(Command):
    def execute(self, operand1, operand2):
        result = operand1 + operand2
        add_to_history(f"{operand1} + {operand2}", result)
        print(f"Result: {result}")

class SubtractCommand(Command):
    def execute(self, operand1, operand2):
        result = operand1 - operand2
        add_to_history(f"{operand1} - {operand2}", result)
        print(f"Result: {result}")

class MultiplyCommand(Command):
    def execute(self, operand1, operand2):
        result = operand1 * operand2
        add_to_history(f"{operand1} * {operand2}", result)
        print(f"Result: {result}")

class DivideCommand(Command):
    def execute(self, operand1, operand2):
        if operand2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = operand1 / operand2
        add_to_history(f"{operand1} / {operand2}", result)
        print(f"Result: {result}")
