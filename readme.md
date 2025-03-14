ADVANCED PYTHON CALCULATOR

Overview:

This project is an advanced Python-based calculator application designed to demonstrate professional software development practices. It features a command-line interface (REPL) that allows users to perform arithmetic operations such as addition, subtraction, multiplication, and division. The application supports dynamic plugin loading, enabling users to extend its functionality by adding new commands via plugins without modifying the core codebase. It also manages a calculation history using Pandas, allowing users to view, save, and delete past calculations.
The project employs object-oriented programming principles, including the use of design patterns such as the Command pattern to handle different operations. It uses logging to track application activities and errors, and configuration is dynamically loaded through environment variables. The application is designed with testability in mind, achieving high code quality through unit tests with Pytest and adhering to PEP 8 standards using Pylint. The project also leverages Git for version control, and continuous integration tools like GitHub Actions ensure that code passes all tests before deployment.

Setup and Usage Instructions:

To get my code running and make calculator application running, follow these steps:

Open terminal and Clone my Repo into your desired location.

cd to midterm-calc.

Install all the required dependencies stated in requirements.txt file

Before installing make sure you have the virtual environment created and activated. Use these commands:

       Python3 -m venv venv and to activate source venv/bin/activate

5)   Now use pip install -r requirements.txt to install all dependencies.


Using Calculator application:

In terminal i.e. command line interface, enter python main.py, which will launch the REPL interface which is stated as a requirement for this project. The REPL interface will read, evaluate, print and loop until “exit” command is entered.

Calculator Commands:


 add - performs addition. Ex: add 2 3

subtract- performs subtraction of two numbers

multiply- performs multiplication of two numbers  

divide- performs division of two numbers

history- this will fetch history of calculations where the user can save load and clear history.

exit- exits the calculator application.

Note: All the commands are case-sensitive.

Functionalities:


Design Patterns:

Design Patterns (Command Pattern):

In app/commands/init.py, the abstract class Command and its concrete subclasses (e.g., AddCommand, SubtractCommand, etc.) implement the Command Pattern, which encapsulates each arithmetic operation as an object.

In app/init.py, the CommandHandler registers and executes these command objects, decoupling the invoker from the operation's implementation.

Similarly, in app/plugins/greet/init.py, the GreetCommand subclass extends Command to provide plugin functionality, further exemplifying the pattern's flexibility in extending application features.



Design Patterns Facade Pattern – Implemented in history management to simplify access to complex underlying functionality.

Factory Method – Implemented in app/init.py to enable creation of objects based on input type.



Environment Variables:

In app/init.py, environment variables are loaded using the load_dotenv() function and the custom method load_environment_variables(), which collects all variables from the OS environment into a dictionary.

This allows the application to dynamically configure its behavior based on the environment (e.g., setting ENVIRONMENT to PRODUCTION, TESTING, or DEVELOPMENT).


Logging:

Logging is configured in app/init.py using the logging and logging.config modules, which set up detailed log messages throughout the application.


This centralized logging ensures that application events, errors, and state changes are consistently recorded, aiding debugging and monitoring.


Try/Catch, EAFP, and LBYL:

The code demonstrates EAFP in app/commands/init.py with the execute_command method, where it attempts to execute a command and catches a KeyError if the command is not found:

def execute_command(self, command_name: str, operand1, operand2):

    try:

        self.commands[command_name].execute(operand1, operand2)

    except KeyError:

        print(f"No such command: {command_name}")



Meanwhile, LBYL is used in the DivideCommand (in app/commands/init.py) where it explicitly checks if the divisor is zero before proceeding with division, thus preventing errors proactively.

Together, these techniques illustrate two approaches to error handling: attempting an action and handling failures (EAFP) versus checking conditions before acting (LBYL).


REPL:

The application implements a REPL (Read-Eval-Print Loop) in the start() method of app/init.py, allowing continuous user interaction through the command line.

def start(self):

    while True:

        cmd_input = input(">>> ").strip()

        # ... process the input and execute commands


This loop continuously accepts user commands, evaluates them (by parsing operands and command names), and prints results, making the application interactive and user-driven.


Plugins:

The project supports a plugin system to extend functionality without modifying core code, as seen in app/init.py with the load_plugins() and register_plugin_commands() methods.

For example, the load_plugins() method dynamically discovers plugin modules from the app/plugins directory:


def load_plugins(self):

    plugins_package = 'app.plugins'

    plugins_path = plugins_package.replace('.', '/')

    if not os.path.exists(plugins_path):

        logging.warning(f"Plugins directory '{plugins_path}' not found.")

        return

    for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):

        if is_pkg:

            try:

                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')

                self.register_plugin_commands(plugin_module, plugin_name)

            except ImportError as e:

                logging.error(f"Error importing plugin {plugin_name}: {e}")



In app/plugins/greet/init.py, the GreetCommand is defined as a plugin that extends Command, demonstrating how new functionality can be added seamlessly via plugins.


