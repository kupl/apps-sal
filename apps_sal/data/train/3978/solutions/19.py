import unittest


def check_for_factor(base, factor):
    return base % factor == 0


class TestCheckForFactor(unittest.TestCase):
    def test_check_for_factor_should_return_true_when_factor_is_divided_by_base(self):
        base, factor = 10, 2
        actual = check_for_factor(base, factor)
        self.assertEqual(actual, True)

    def test_check_for_factor_should_return_false_when_factor_is_not_divided_by_base(self):
        base, factor = 9, 2
        actual = check_for_factor(base, factor)
        self.assertEqual(actual, False)
