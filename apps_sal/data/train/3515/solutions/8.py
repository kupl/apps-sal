from string import ascii_lowercase
from operator import add, sub
from itertools import starmap
from re import sub as rsub


def change(text, key, o):
    tmp = dict.fromkeys(key)
    cipher = ''.join(tmp) + ''.join(c for c in ascii_lowercase if c not in tmp)
    D = {c: i for i, c in enumerate(cipher)}
    def a(i, c): return cipher[o(D[c], i) % 26]
    def b(i, c): return cipher[o(D[c.lower()], i) % 26].upper()
    def f(i, c): return a(i, c) if c.islower() else b(i, c) if c.isupper() else c
    def g(w): return ''.join(starmap(f, enumerate(w.group(), 1)))
    return rsub(r"[a-zA-z]+", g, text)


def encode(text, key):
    return change(text, key, add)


def decode(text, key):
    return change(text, key, sub)
