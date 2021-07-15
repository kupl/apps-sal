import unittest


def greet(name):
    return "Hello, {} how are you doing today?".format(name)
    
    
class TestGreet(unittest.TestCase):
    def test_greet(self):
        name = 'Ryan'
        actual = greet(name)
        self.assertEqual(actual, "Hello, Ryan how are you doing today?")

