import re


def move_vowels(input):
    return ''.join((''.join(l) for l in zip(*re.findall('([^aeiou])?([aeiou])?', input))))
