import re


def unscramble_eggs(word):
    return re.sub('([^aeiouAEIOU])egg', '\\1', word)
