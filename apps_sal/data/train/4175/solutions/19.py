import unittest


def repeater(string, n):
    return string * n


class TestRepeater(unittest.TestCase):
    def test_repeater(self):
        string, n = 'a', 5
        actual = repeater(string, n)
        self.assertEqual(actual, 'aaaaa')
