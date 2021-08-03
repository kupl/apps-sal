from string import ascii_lowercase


def abacaba(k):
    for i, c in enumerate(reversed(ascii_lowercase)):
        p = 2 ** (25 - i)
        if k == p:
            return c
        if k > p:
            k -= p
