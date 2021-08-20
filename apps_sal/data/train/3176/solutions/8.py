import re


def to_cents(amount):
    if not re.match('^\\$(0|[1-9]+\\d*)\\.\\d{2}\\Z', amount):
        return None
    return int(re.sub('[\\$\\.]', '', amount))
