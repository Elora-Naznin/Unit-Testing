# File: test_calculator.py

import unittest
from calculator import divide

class TestCalculator(unittest.TestCase):

    def test_divide_positive_numbers(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_negative_numbers(self):
        result = divide(-12, -3)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()
