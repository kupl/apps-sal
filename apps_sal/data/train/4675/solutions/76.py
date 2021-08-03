import unittest


def set_alarm(employed, vacation):
    return employed and not vacation


class TestSetAlarm(unittest.TestCase):
    def test_should_return_false_when_employed_is_true_and_vacation_is_true(self):
        self.assertEqual(set_alarm(employed=True, vacation=True), False)

    def test_should_return_false_when_employed_is_false_and_vacation_is_false(self):
        self.assertEqual(set_alarm(employed=False, vacation=False), False)

    def test_should_return_false_when_employed_is_false_and_vacation_is_true(self):
        self.assertEqual(set_alarm(employed=False, vacation=True), False)

    def test_should_return_false_when_employed_is_true_and_vacation_is_false(self):
        self.assertEqual(set_alarm(employed=True, vacation=False), True)
