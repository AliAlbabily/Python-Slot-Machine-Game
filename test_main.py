import unittest
from unittest.mock import patch
from main import deposit

class TestProgram(unittest.TestCase):
    
    # My test cases

    @patch("builtins.input", side_effect=["50"]) # the first time input() is called, it will return "50"
    def test_valid_deposit_input(self, mock_input):
        result = deposit()
        self.assertEqual(result, 50)  # checks if the result returned by deposit() is equal to 50


if __name__ == "__main__":
    unittest.main()