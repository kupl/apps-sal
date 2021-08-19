import re


def repl(m):
    return m[0] + ('err' if m[0].islower() else 'ERR')


def err_bob(s):
    return re.sub('(?![aeiou])[a-z]\\b', repl, s, flags=re.I)
