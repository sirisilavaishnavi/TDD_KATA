import unittest
from String_Calculator import *

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()

    def EmptyStringCalculator():
        self.assertEqual(self.calc.add(""), 0)


if __name__ == "_main_":
    unittest.main()
