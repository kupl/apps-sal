import unittest


def reverse_number(n):
    revered_num = int(str(abs(n))[::-1])

    if n < 0:
        return int('-{}'.format(revered_num))

    return revered_num

    
class TestReverseNumber(unittest.TestCase):
    def test_reverse_number_with_n_is_one_digit(self):
        n = 5
        actual = reverse_number(n)
        self.assertEqual(actual, 5)

    def test_reverse_number_with_negative_sign(self):
        n = -123
        actual = reverse_number(n)
        self.assertEqual(actual, -321)

    def test_reverse_number_without_any_sign(self):
        n = 123
        actual = reverse_number(n)
        self.assertEqual(actual, 321)

    def test_reverse_number_should_return_1_when_given_n_is_1000(self):
        n = 1000
        actual = reverse_number(n)
        self.assertEqual(actual, 1)

