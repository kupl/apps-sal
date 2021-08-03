import unittest


def hello(name=None):
    return 'Hello, {}!'.format(name.capitalize() if name else 'World')


class TestHello(unittest.TestCase):
    def test_hello_should_return_default_string_with_not_given_name(self):
        self.assertEqual(hello(None), 'Hello, World!')

    def test_hello_should_return_default_string_with_given_name_is_empty_string(self):
        self.assertEqual(hello(''), 'Hello, World!')

    def test_hello_with_only_lower_case(self):
        self.assertEqual(hello('abcde'), 'Hello, Abcde!')

    def test_hello_with_mixed(self):
        self.assertEqual(hello('aBcDe'), 'Hello, Abcde!')
