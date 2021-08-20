import unittest


def say_hello(name, city, state):
    name = ' '.join(name)
    city_and_state = ', '.join([city, state])
    return f'Hello, {name}! Welcome to {city_and_state}!'


class TestSayHello(unittest.TestCase):

    def test_say_hello(self):
        (name, city, state) = (['John', 'Smith'], 'Phoenix', 'Arizona')
        actual = say_hello(name, city, state)
        self.assertEqual(actual, 'Hello, John Smith! Welcome to Phoenix, Arizona!')
