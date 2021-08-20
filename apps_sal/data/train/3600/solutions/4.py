import re


def move_vowels(input):
    (consonants, vowels) = (re.sub('[aeiou]', '', input), re.sub('[^aeiou]', '', input))
    return consonants + vowels
