import unittest


def tidyNumber(n):
    return all((False for ele in zip(str(n), str(n)[1:]) if int(ele[1]) - int(ele[0]) < 0))


class TestTidyNumber(unittest.TestCase):

    def test_should_return_true_when_given_n_is_12(self):
        n = 12
        actual = tidyNumber(n)
        self.assertEqual(actual, True)

    def test_should_return_false_when_given_n_is_102(self):
        n = 102
        actual = tidyNumber(n)
        self.assertEqual(actual, False)
