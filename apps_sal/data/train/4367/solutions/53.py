import unittest


def area_or_perimeter(length, width):
    return length * width if length == width else 2 * length + 2 * width


class TestAreaOrPerimeter(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area_or_perimeter(length=4, width=4), 16)

    def test_perimeter(self):
        self.assertEqual(area_or_perimeter(length=10, width=4), 28)
