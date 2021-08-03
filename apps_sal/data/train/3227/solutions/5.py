from string import ascii_lowercase as az


def to_lover_case(s):
    return ''.join('LOVE'[az.index(c) % 4] if c in az else c for c in s.lower())
