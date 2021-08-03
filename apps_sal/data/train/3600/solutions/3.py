import re


def move_vowels(input):
    consonants = re.sub(r'[aeiou]', '', input)
    vowels = re.sub(r'[^a^e^i^o^u]', '', input)
    return consonants + vowels
