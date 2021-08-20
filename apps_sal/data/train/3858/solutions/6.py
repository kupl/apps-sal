import re


def unscramble_eggs(word):
    pattern = re.compile('([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])egg')
    return re.sub(pattern, '\\1', word)
