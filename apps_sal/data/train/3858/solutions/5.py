import re


def unscramble_eggs(word):
    return re.sub(r'([^aeiouAEIOU])egg', r'\1', word)
