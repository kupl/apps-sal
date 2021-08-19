import re


def unscramble_eggs(word):
    return re.sub('(?<=[^aeiou])egg', '', word)
