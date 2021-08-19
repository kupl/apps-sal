import unittest
HELLO = 'Hello'
WORLD = 'World'
EXCLAMATION_MARK = '!'
DEFAULT_TEMPLATE = '{}, {}{}'


def hello(name=None):

    def get_hello(word, hello_string=HELLO, exclamation_mark=EXCLAMATION_MARK):
        return DEFAULT_TEMPLATE.format(hello_string, word, exclamation_mark)
    return get_hello(word=name.title()) if name else get_hello(word=WORLD)


class TestHello(unittest.TestCase):

    def test_hello_should_return_default_string_with_not_given_name(self):
        self.assertEqual(hello(None), 'Hello, World!')

    def test_hello_should_return_default_string_with_given_name_is_empty_string(self):
        self.assertEqual(hello(''), 'Hello, World!')

    def test_hello_with_only_lower_case(self):
        self.assertEqual(hello('abcde'), 'Hello, Abcde!')

    def test_hello_with_mixed(self):
        self.assertEqual(hello('aBcDe'), 'Hello, Abcde!')
