import re


def to_cents(amount):
    m = re.match('\\$(\\d+)\\.(\\d\\d)\\Z', amount)
    return int(m.expand('\\1\\2')) if m else None
