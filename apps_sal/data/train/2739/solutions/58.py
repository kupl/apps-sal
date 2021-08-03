import unittest


def cube_odd(arr):
    def _is_none_condition():
        return any(True if not isinstance(ele, int)
                           or ele is True
                   or ele is False
                   else False for ele in arr)
    if _is_none_condition():
        return
    return sum(ele ** 3 if ele % 2 == 1 else 0 for ele in arr)


class TestCubeOdd(unittest.TestCase):
    def test_should_return_none_when_any_of_the_values_are_not_numbers(self):
        arr = ["a", 12, 9, "z", 42]
        actual = cube_odd(arr)
        self.assertEqual(actual, None)

    def test_cube_odd(self):
        arr = [1, 2, 3, 4]
        actual = cube_odd(arr)
        self.assertEqual(actual, 28)
