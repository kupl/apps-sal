from re import split


def vowel_shift(text, n):
    if text == None:
        return None
    parts = split('([aeiouAEIOU])', text)
    return ''.join((parts[i if i % 2 == 0 else (i - 2 * n) % (len(parts) - 1)] for i in range(len(parts))))
