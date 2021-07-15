import re

def move_vowels(input): 
    consonants, vowels = re.sub(r'[aeiou]', '', input), re.sub(r'[^aeiou]', '', input)
    return consonants + vowels
