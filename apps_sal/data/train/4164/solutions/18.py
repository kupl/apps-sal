from collections import Counter


def first_non_repeating_letter(s):
    for (c, v) in sorted(Counter(s).most_common(), key=lambda t: t[1]):
        if v == 1 and c.swapcase() not in s or not c.isalpha():
            return c
    return ''
