import re


def key(t):
    i, s = t
    return (s.count('#'), s.count('.'), len(re.split(r'(?!<^)[ .#]+', s)), s != '*', i)


def compare(*args):
    return max(enumerate(args), key=key)[1]
