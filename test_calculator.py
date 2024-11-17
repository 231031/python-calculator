import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(0, -2), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(-2, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 3), 1)
        self.assertEqual(self.calc.divide(-4, 4), -1)
        self.assertEqual(self.calc.divide(2, 4), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)
        self.assertEqual(self.calc.modulo(-3, 2), 1)
        self.assertEqual(self.calc.modulo(-3, -2), -1)
        self.assertEqual(self.calc.modulo(15, -7), -6)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()