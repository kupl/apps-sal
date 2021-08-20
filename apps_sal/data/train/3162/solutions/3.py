def charsum(s):
    return bool(s) and s.isalpha() and sum((ord(c) for c in s.upper()))


def compare(s1, s2):
    return charsum(s1) == charsum(s2)
