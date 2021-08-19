import unittest


def two_decimal_places(n):
    return round(n, 2)


class TestTwoDecimalPlaces(unittest.TestCase):

    def test_two_decimal_places(self):
        n = 4.659725356
        actual = two_decimal_places(n)
        self.assertEqual(actual, 4.66)
