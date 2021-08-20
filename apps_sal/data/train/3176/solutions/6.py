import re


def to_cents(amount):
    return int(re.sub('\\$|\\.', '', amount)) if re.search('^\\$\\d+\\.\\d{1,2}\\Z', amount) else None
