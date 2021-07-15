import unittest


def is_even(n):
    return n % 2 == 0
    
    
class TestIsEven(unittest.TestCase):
    def test_is_even_with_even(self):
        self.assertTrue(is_even(4))

    def test_is_even_with_odd(self):
        self.assertFalse((is_even(5)))

