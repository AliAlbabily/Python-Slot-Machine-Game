import unittest
from unittest.mock import patch
from main import deposit

class TestProgram(unittest.TestCase):
    
    # My test cases

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


if __name__ == "__main__":
    unittest.main()