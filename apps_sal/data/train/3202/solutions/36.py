import unittest
HELLO_BOSS_MSG = 'Hello boss'
HELLO_GUEST_MSG = 'Hello guest'


def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'


class TestGreet(unittest.TestCase):

    def test_should_return_hello_boss_msg_when_names_equals_owner(self):
        (name, owner) = ('Daniel', 'Daniel')
        actual = greet(name, owner)
        self.assertEqual(actual, 'Hello boss')

    def test_should_return_hello_guest_msg_when_names_equals_owner(self):
        (name, owner) = ('Daniel', 'Guest')
        actual = greet(name, owner)
        self.assertEqual(actual, 'Hello guest')
