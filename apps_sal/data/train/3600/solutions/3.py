import re


def move_vowels(input):
    consonants = re.sub('[aeiou]', '', input)
    vowels = re.sub('[^a^e^i^o^u]', '', input)
    return consonants + vowels
