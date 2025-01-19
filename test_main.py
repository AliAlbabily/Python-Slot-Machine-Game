import unittest
from unittest.mock import patch
from main import deposit
from main import main

class TestProgram(unittest.TestCase):
    
    # My test cases

    # def deposit()
    @patch("builtins.input", side_effect=["50"]) # the first time input() is called, it will return "50"
    def test_deposit_valid_input(self, mock_input):
        result = deposit()
        self.assertEqual(result, 50)  # checks if the result returned by deposit() is equal to 50

    @patch("builtins.input", side_effect=["-10", "0", "25"])
    def test_deposit_invalid_then_valid_input(self, mock_input):
        result = deposit()
        self.assertEqual(result, 25)  # assert the function eventually returns a valid amount after invalid inputs.

    @patch("builtins.input", side_effect=["abc", "50"])
    def test_non_numeric_then_valid_input(self, mock_input):
        result = deposit()
        self.assertEqual(result, 50)  # assert the function handles non-numeric input and then a valid amount.

    # def main()
    @patch("builtins.input", side_effect=["q"])  # Simulates quitting immediately
    @patch("main.deposit", return_value=100)    # Mock deposit to return 100
    @patch("builtins.print")                    # Mock print to capture outputs
    def test_quit_immediately(self, mock_print, mock_deposit, mock_input):
        main()  # Run main function
        mock_deposit.assert_called_once()       # Ensure deposit() is called
        mock_print.assert_any_call("Current balance is $100")  # Check initial balance message
        mock_print.assert_any_call("You left with $100")       # Check final balance message


if __name__ == "__main__":
    unittest.main()