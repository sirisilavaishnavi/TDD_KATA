import unittest
import pytest
from String_Calculator import *

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_one_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newline_delimiter(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2;5"), 8)
        
    def test_negative_number_exception(self):
        with pytest.raises(ValueError, match="Negative numbers not allowed: -2"):
            self.assertEqual(self.calc.add("1,-2"), 1)
        
    def test_multiple_negative_numbers(self):
        with pytest.raises(ValueError, match="Negative numbers not allowed: -1,-2,-3,-4"):
            self.assertEqual(self.calc.add("-1,-2,-3,-4,5"), 5)
    
    def test_ignore_gt_1000_numbers(self):
        self.assertEqual(self.calc.add("2,3,1002"), 5)

    def test_n_length_delimiter(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)
    
    def test_multiple_set_delimiter(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)

if __name__ == "__main__":
    unittest.main()
