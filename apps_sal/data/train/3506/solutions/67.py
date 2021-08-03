import unittest

VOWEL = {'a', 'e', 'i', 'o', 'u', 'y'}


def vowel_indices(word):
    return [index for index, ele in enumerate(word, 1) if ele.lower() in VOWEL]


class TestVowelIndices(unittest.TestCase):
    def test_vowel_indices(self):
        word = 'Super'
        actual = vowel_indices(word)
        self.assertEqual(actual, [2, 4])
