import re


def to_cents(amount):
    price = re.match(r'^\$(\d+)\.(\d{1,2})\Z', amount)
    return int(price.expand(r'\1\2')) if price else None
