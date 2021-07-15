import unittest


def find_digit(num, nth):
    num = abs(num)
    if nth <= 0:
        return -1
    if len(str(num)) < nth:
        return 0
    return int(str(num)[::-1][nth-1])
    
    
class TestFindDigit(unittest.TestCase):
    def test_should_return_negative_one_given_nth_is_negative(self):
        negative_nth = -123
        self.assertEqual(find_digit(num=-12345, nth=negative_nth), -1)

    def test_should_return_negative_one_given_nth_is_zero(self):
        zero = 0
        self.assertEqual(find_digit(num=-12345, nth=zero), -1)

    def test_should_return_0_given_nth_is_greater_than_length_of_num(self):
        self.assertEqual(find_digit(num=0, nth=20), 0)

    def test_should_return_0_given_nth_is_greater_than_length_of_num_with_negative_sign(self):
        self.assertEqual(find_digit(num=-456, nth=4), 0)

    def test_should_return_4_when_given_num_is_5673(self):
        self.assertEqual(find_digit(num=5673, nth=4), 5)

