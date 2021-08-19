import unittest


def get_age(age):
    return int(age.split()[0])


class TestGetAge(unittest.TestCase):

    def test_should_return_2_when_string_age_has_2(self):
        age = '2 years old'
        actual = get_age(age)
        self.assertEqual(actual, 2)
