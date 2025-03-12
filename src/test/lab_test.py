import unittest
from src.main.lab import (
    equal_to,
    greater_than,
    less_than,
    greater_than_or_equal_to,
    less_than_or_equal_to,
    not_equal_to,
    logical_and,
    logical_or,
    logical_not
)

class TestLab(unittest.TestCase):
    def test_equal_to(self):
        self.assertTrue(equal_to(5, 5))
        self.assertFalse(equal_to(5, 10))

    def test_greater_than(self):
        self.assertTrue(greater_than(10, 5))
        self.assertFalse(greater_than(5, 10))

    def test_less_than(self):
        self.assertTrue(less_than(3, 6))
        self.assertFalse(less_than(6, 3))

    def test_greater_than_or_equal_to(self):
        self.assertTrue(greater_than_or_equal_to(7, 7))
        self.assertFalse(greater_than_or_equal_to(6, 7))

    def test_less_than_or_equal_to(self):
        self.assertTrue(less_than_or_equal_to(4, 4))
        self.assertFalse(less_than_or_equal_to(5, 4))

    def test_not_equal_to(self):
        self.assertTrue(not_equal_to(2, 4))
        self.assertFalse(not_equal_to(3, 3))

    def test_logical_and(self):
        self.assertTrue(logical_and(True, True))
        self.assertFalse(logical_and(True, False))

    def test_logical_or(self):
        self.assertTrue(logical_or(True, False))
        self.assertFalse(logical_or(False, False))

    def test_logical_not(self):
        self.assertTrue(logical_not(False))
        self.assertFalse(logical_not(True))

if __name__ == '__main__':
    unittest.main()
