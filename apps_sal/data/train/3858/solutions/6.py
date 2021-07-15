import re

def unscramble_eggs(word):
    # Geggoodegg Legguceggkegg!
    pattern = re.compile(r'([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])egg')
    return re.sub(pattern, r'\1', word)
