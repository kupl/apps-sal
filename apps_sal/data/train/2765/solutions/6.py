import re


def key(t):
    i, s = t
    return (s.count('


def compare(*args):
    return max(enumerate(args), key=key)[1]
