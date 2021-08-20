import re


def to_cents(amount):
    price = re.match('^\\$(\\d+)\\.(\\d{1,2})\\Z', amount)
    return int(price.expand('\\1\\2')) if price else None
