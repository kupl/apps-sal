import unittest


def halving_sum(n):
    temp = []
    while True:
        if n == 1:
            break
        temp.append(n)
        n = n // 2
    return sum(temp) + 1


class TestHalvingSum(unittest.TestCase):

    def test_halving_sum_when_given_n_is_25(self):
        n = 25
        actual = halving_sum(n)
        self.assertEqual(actual, 47)

    def test_halving_sum_when_given_n_is_127(self):
        n = 127
        actual = halving_sum(n)
        self.assertEqual(actual, 247)
