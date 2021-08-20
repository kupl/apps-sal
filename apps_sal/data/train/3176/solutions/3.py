import re


def to_cents(amount):
    matched = re.search('\\A\\$(\\d+).(\\d{2})\\Z', amount)
    if matched:
        return int('{}{}'.format(*matched.groups()))
