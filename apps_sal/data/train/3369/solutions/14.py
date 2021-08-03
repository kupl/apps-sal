import unittest


def move(position, roll):
    return position + roll * 2


class TestMove(unittest.TestCase):
    def test_move(self):
        self.assertEqual(move(position=0, roll=4), 8)
