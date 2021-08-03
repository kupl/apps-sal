import unittest


def house_numbers_sum(inp):
    result = 0
    for ele in inp:
        if ele == 0:
            break
        result += ele
    return result


class TestHoseNumbersSum(unittest.TestCase):
    def test_should_return_0_when_given_inp_first_element_is_0(self):
        inp = [0, 1, 2, 3, 4, 5]
        actual = house_numbers_sum(inp)
        self.assertEqual(actual, 0)

    def test_should_return_sum_of_all_elemnt_when_given_inp_last_element_is_0(self):
        inp = [1, 2, 3, 4, 5, 0]
        actual = house_numbers_sum(inp)
        self.assertEqual(actual, 15)

    def test_should_return_sum_of_element_until_0_when_given_inp_has_0_in_middle(self):
        inp = [1, 2, 0, 4, 5]
        actual = house_numbers_sum(inp)
        self.assertEqual(actual, 3)
