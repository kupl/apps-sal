from itertools import zip_longest


def encrypt(text, n):
    s = text
    if s:
        for _ in range(n):
            s = s[1::2] + s[::2]
    return s


def decrypt(encrypted_text, n):
    s = encrypted_text
    if s:
        m = len(s) // 2
        for _ in range(n):
            s = ''.join(c for s in zip_longest(s[m:], s[:m], fillvalue='') for c in s)
    return s
