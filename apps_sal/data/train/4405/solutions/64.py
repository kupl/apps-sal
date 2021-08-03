import unittest


def is_palindrome(string):
    string = str(string)
    return string == string[::-1]


class TestPalindromeStrings(unittest.TestCase):
    def test_is_palindrome_with_not_palindrome_string(self):
        string = 'walter'
        actual = is_palindrome(string)
        self.assertEqual(actual, False)

    def test_is_palindrome_with_palindrome_string(self):
        string = 'anna'
        actual = is_palindrome(string)
        self.assertEqual(actual, True)

    def test_is_palindrome_with_not_palindrome_integer_value(self):
        string = 12345
        actual = is_palindrome(string)
        self.assertEqual(actual, False)

    def test_is_palindrome_with_palindrome_integer_value(self):
        string = 12321
        actual = is_palindrome(string)
        self.assertEqual(actual, True)
