import unittest

JAVA = 'Java'
COFFEE = 'Coffee'
SCRIPT = 'Script'
MOCHA_MISSING = 'mocha_missing!'


def caffeineBuzz(n):
    if n % 3 == 0:
        language = JAVA
        if n % 4 == 0:
            language = COFFEE
            if n % 2 == 0:
                language += SCRIPT
        elif n % 2 == 0:
            language += SCRIPT
        return language
    else:
        return MOCHA_MISSING



class TestCaffeineBuzz(unittest.TestCase):
    def test_should_return_java_when_given_n_is_divisible_by_3(self):
        n = 3
        actual = caffeineBuzz(n)
        self.assertEqual(actual, 'Java')

    def test_should_return_coffee_script_when_given_n_is_divisible_by_3_or_divisible_by_and_divisible_by_4_and_divisible_by_2(self):
        n = 12
        actual = caffeineBuzz(n)
        self.assertEqual(actual, 'CoffeeScript')

    def test_should_return_coffee_script_when_given_n_is_divisible_by_3_or_divisible_by_and_not_divisible_by_4_and_divisible_by_2(self):
        n = 6
        actual = caffeineBuzz(n)
        self.assertEqual(actual, 'JavaScript')

    def test_should_return_moch_missing_when_given_n_is_1(self):
        n = 1
        actual = caffeineBuzz(n)
        self.assertEqual(actual, 'mocha_missing!')

