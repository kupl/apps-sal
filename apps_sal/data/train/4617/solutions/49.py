import unittest


def powers_of_two(n):

    return [2 ** i for i in range(n + 1)]
    
    
class TestPowerOfTwo(unittest.TestCase):
    def test_power_of_two(self):
        n = 4
        actual = power_of_two(n)
        self.assertEqual(actual, [1, 2, 4, 8, 16])

