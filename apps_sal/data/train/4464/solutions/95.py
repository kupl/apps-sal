import unittest


def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False


class TestFeast(unittest.TestCase):
    def test_should_return_false_when_given_first_char_and_end_char_of_beast_name_is_not_same_with_dish(self):
        beast, dish = "brown bear", "bear claw"
        actual = feast(beast, dish)
        self.assertEqual(actual, False)

    def test_should_return_true_when_given_first_char_and_end_char_of_beast_name_is_same_with_dish(self):
        beast, dish = "great blue heron", "garlic naan"
        actual = feast(beast, dish)
        self.assertEqual(actual, True)
