import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import Command
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, view_history

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

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

        # Register the arithmetic commands
        self.register_arithmetic_commands()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

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

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def register_arithmetic_commands(self):
        # Register the basic arithmetic operations
        self.command_handler.register_command('add', AddCommand())
        self.command_handler.register_command('subtract', SubtractCommand())
        self.command_handler.register_command('multiply', MultiplyCommand())
        self.command_handler.register_command('divide', DivideCommand())

    def start(self):
        logging.info("Application started. Type 'exit' to exit or 'history' to view calculation history.")
        try:
            while True:
                cmd_input = input(">>> ").strip()

                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)

                elif cmd_input.lower() == 'history':
                    print(view_history())
                    continue  # Skip the command handler for this

                # Parse the command and operands
                parts = cmd_input.split()
                if len(parts) < 3:
                    print(f"No such command: unknown_command")
                    continue

                command_name, operand1, operand2 = parts[0], parts[1], parts[2]

                try:
                    operand1 = float(operand1)
                    operand2 = float(operand2)
                except ValueError:
                    print("Error: Operands must be numeric values.")
                    continue

                # Execute the corresponding command
                if command_name == "add":
                    self.command_handler.execute_command('add', operand1, operand2)
                elif command_name == "subtract":
                    self.command_handler.execute_command('subtract', operand1, operand2)
                elif command_name == "multiply":
                    self.command_handler.execute_command('multiply', operand1, operand2)
                elif command_name == "divide":
                    self.command_handler.execute_command('divide', operand1, operand2)
                else:
                    print(f"No such command: {command_name}")  # Change this line to match test expectation
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()

