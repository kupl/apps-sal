import unittest


def odd_count(n):
    return n // 2


class TestOddCount(unittest.TestCase):
    def test_should_return_7_when_given_n_is_15(self):
        n = 15
        actual = odd_count(n)
        self.assertEqual(actual, 7)

    def test_should_return_7511_when_given_n_is_15023(self):
        n = 15023
        actual = odd_count(n)
        self.assertEqual(actual, 7511)
