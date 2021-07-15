import unittest

RIGHT_SIDE_WINS = "Right side wins!"
LEFT_SIDE_WINS = "Left side wins!"
FIGHT_AGAIN = "Let's fight again!"


LEFT_LETTERS = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1,
}

RIGHT_LETTERS = {
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1,
}


def alphabet_war(fight):
    left = []
    right = []
    for ele in fight:
        if ele in LEFT_LETTERS:
            left.append(LEFT_LETTERS[ele])
        elif ele in RIGHT_LETTERS:
            right.append(RIGHT_LETTERS[ele])

    if sum(left) == sum(right):
        return FIGHT_AGAIN
    else:
        return LEFT_SIDE_WINS if sum(left) > sum(right) else RIGHT_SIDE_WINS
    
    
class TestAlphabetWar(unittest.TestCase):
    def test_alphabet_war_on_right_side_wins(self):
        fight = 'z'
        actual = alphabet_war(fight)
        self.assertEqual(actual, RIGHT_SIDE_WINS)

    def test_alphabet_war_on_left_side_wins(self):
        fight = 'wq'
        actual = alphabet_war(fight)
        self.assertEqual(actual, LEFT_SIDE_WINS)

    def test_alphabet_war_on_fight_again(self):
        fight = 'zdqmwpbs'
        actual = alphabet_war(fight)
        self.assertEqual(actual, FIGHT_AGAIN)

