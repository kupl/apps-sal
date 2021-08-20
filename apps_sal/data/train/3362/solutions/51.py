import unittest


def sum_mix(input_array):
    return sum((int(element) if isinstance(element, str) else element for element in input_array))


class TestSumMix(unittest.TestCase):

    def test_sum_mix_with_elements_are_only_integer(self):
        self.assertEqual(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

    def test_sum_mix_with_elements_are_only_string(self):
        self.assertEqual(sum_mix(['1', '2', '3', '4', '5']), 15)

    def test_sum_mix_with_elements_are_integers_or_string(self):
        self.assertEqual(sum_mix(['1', 2, '3', 4, '5']), 15)
