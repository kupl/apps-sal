import re
from collections import deque


def vowel_shift(text, n):
    try:
        tokens = re.split('([aeiouAEIOU])', text)
        if len(tokens) > 1:
            vowels = deque(tokens[1::2])
            vowels.rotate(n)
            tokens[1::2] = vowels
        return ''.join(tokens)
    except TypeError:
        return None
