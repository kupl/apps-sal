import re


def to_cents(amount):
    return int(re.sub("\D", "", amount)) if re.match("\$\d*\.\d{2}\Z", amount) else None
