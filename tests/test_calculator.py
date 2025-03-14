import pytest
from unittest.mock import patch
from app import App

class TestCalculatorOperations:
    @patch("builtins.input", side_effect=["add 2 3", "exit"])
    @patch("builtins.print")
    def test_add_command(self, mock_print, mock_input):
        # "add 2 3" should print "Result: 5.0"
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Result: 5.0")

    @patch("builtins.input", side_effect=["subtract 5 2", "exit"])
    @patch("builtins.print")
    def test_subtract_command(self, mock_print, mock_input):
        # "subtract 5 2" should print "Result: 3.0"
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Result: 3.0")

    @patch("builtins.input", side_effect=["multiply 2 3", "exit"])
    @patch("builtins.print")
    def test_multiply_command(self, mock_print, mock_input):
        # "multiply 2 3" should print "Result: 6.0"
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Result: 6.0")

    @patch("builtins.input", side_effect=["divide 6 3", "exit"])
    @patch("builtins.print")
    def test_divide_command(self, mock_print, mock_input):
        # "divide 6 3" should print "Result: 2.0"
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Result: 2.0")

    @patch("builtins.input", side_effect=["divide 6 0", "exit"])
    @patch("builtins.print")
    def test_divide_by_zero(self, mock_print, mock_input):
        # "divide 6 0" should print an error message for division by zero.
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Error: Division by zero is not allowed.")

    @patch("builtins.input", side_effect=["add 2 a", "exit"])
    @patch("builtins.print")
    def test_invalid_operand(self, mock_print, mock_input):
        # "add 2 a" should print an error message for non-numeric operand.
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("Error: Operands must be numeric values.")

    @patch("builtins.input", side_effect=["unknown_command 2 3", "exit"])
    @patch("builtins.print")
    def test_unknown_command(self, mock_print, mock_input):
        # An unknown command should print the correct error message.
        with pytest.raises(SystemExit):
            App().start()
        mock_print.assert_any_call("No such command: unknown_command")

