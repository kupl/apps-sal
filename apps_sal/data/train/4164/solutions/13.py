from collections import Counter


def first_non_repeating_letter(string):
    count = Counter((s.lower() for s in string))
    for c in string:
        if count[c.lower()] == 1:
            return c
    return str()
