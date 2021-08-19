import unittest


def angle(n):
    return 180 * (n - 2)


class TestAngle(unittest.TestCase):

    def test_should_return_180_when_given_n_is_3(self):
        self.assertEqual(angle(3), 180)

    def test_should_return_360_when_given_n_is_4(self):
        self.assertEqual(angle(4), 360)

    def test_should_return_540_when_given_n_is_5(self):
        self.assertEqual(angle(5), 540)
