import unittest


def nth_even(n):
    return (n - 1) * 2


class TestNthEven(unittest.TestCase):
    def test_should_0_when_given_n_is_1(self):
        n = 1
        actual = nth_even(n)
        self.assertEqual(actual, 0)

    def test_should_4_when_given_n_is_3(self):
        n = 3
        actual = nth_even(n)
        self.assertEqual(actual, 4)
