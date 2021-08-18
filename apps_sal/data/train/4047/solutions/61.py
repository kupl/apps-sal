import unittest

MAPPING_TABLE = {
    'A': '@',
    'B': '8',
    'C': '(',
    'D': 'D',
    'E': '3',
    'F': 'F',
    'G': '6',
    'H': '
    'I': '!',
    'J': 'J',
    'K': 'K',
    'L': '1',
    'M': 'M',
    'N': 'N',
    'O': '0',
    'P': 'P',
    'Q': 'Q',
    'R': 'R',
    'S': '$',
    'T': '7',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '2',
    ' ': ' '
}


def to_leet_speak(str_):
    return ''.join(MAPPING_TABLE[char] for char in str_)


class TestToLeekSpeak(unittest.TestCase):
    def test_to_leek_speak(self):
        str_ = 'LEET'
        actual = to_leek_speak(str_)
        self.assertEqual(actual, '1337')

    def test_to_leek_speak_with_empty_space(self):
        str_ = 'HELLO WORLD'
        actual = to_leek_speak(str_)
        self.assertEqual(actual, '
