import re


def unscramble_eggs(word):
    pattern = re.compile(r'([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])egg')
    return re.sub(pattern, r'\1', word)
