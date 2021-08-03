import unittest


def tidyNumber(n):
    n = str(n)
    return all(e0 <= e1 for e0, e1 in zip(n, n[1:]))


class TestTidyNumber(unittest.TestCase):
    def test_should_return_true_when_given_n_is_12(self):
        n = 12
        actual = tidyNumber(n)
        self.assertEqual(actual, True)

    def test_should_return_false_when_given_n_is_102(self):
        n = 102
        actual = tidyNumber(n)
        self.assertEqual(actual, False)
