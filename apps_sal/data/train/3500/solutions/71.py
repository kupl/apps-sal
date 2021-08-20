import unittest


def remove_exclamation_marks(s):
    return s.replace('!', '')


class TestRemoveExclamationMarks(unittest.TestCase):

    def test_only_one_exclamation_marks(self):
        s = 'Hello World!'
        actual = remove_exclamation_marks(s)
        self.assertEqual(actual, 'Hello World')

    def test_only_all_exclamation_marks(self):
        s = 'Hello World!'
        actual = remove_exclamation_marks(s)
        self.assertEqual(actual, 'Hello World')
