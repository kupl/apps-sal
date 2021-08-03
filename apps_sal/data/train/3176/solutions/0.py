import re


def to_cents(amount):
    m = re.match(r'\$(\d+)\.(\d\d)\Z', amount)
    return int(m.expand(r'\1\2')) if m else None
