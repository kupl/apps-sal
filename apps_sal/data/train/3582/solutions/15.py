from re import compile, match
REGEX = compile('\\d$')


def is_digit(n):
    m = match(REGEX, n)
    return bool(m) and n[slice(*m.span())] == n
