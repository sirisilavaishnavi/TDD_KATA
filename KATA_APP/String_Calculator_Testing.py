import unittest
from String_Calculator import *

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def EmptyStringCalculator(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_one_number(self):
        self.assertEqual(self.calc.add("1"), 1)
        

if __name__ == "__main__":
    unittest.main()
