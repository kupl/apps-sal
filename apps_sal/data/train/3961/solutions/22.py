import unittest


def say_hello(name):
    return 'Hello, {}'.format(name)


class TestSayHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello('Mr. Spock'), 'Hello, Mr. Spock')
