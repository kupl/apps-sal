from re import compile, match
REGEX = compile('\\$(?P<integer>\\d+)\\.(?P<frac>\\d{0,2})$')


def to_cents(amount):
    m = match(REGEX, amount)
    if m and m.group(0) == amount:
        return int(m.group('integer')) * 100 + int(m.group('frac'))
