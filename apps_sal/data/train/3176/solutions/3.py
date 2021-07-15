import re

def to_cents(amount):
    matched = re.search(r'\A\$(\d+).(\d{2})\Z', amount)
    if matched:
        return int('{}{}'.format(*matched.groups()))
