import unittest


def check_alive(health):
    return True if health > 0 else False
    
    
class TestCheckAlive(unittest.TestCase):
    def test_should_return_true_when_health_is_greater_than_0(self):
        self.assertEqual(check_alive(health=1), True)

    def test_should_return_false_when_health_is_0(self):
        self.assertEqual(check_alive(health=0), False)

    def test_should_return_false_when_health_is_negative_int(self):
        self.assertEqual(check_alive(health=-1), False)

