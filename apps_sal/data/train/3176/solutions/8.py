import re


def to_cents(amount):

    if not re.match(r"^\$(0|[1-9]+\d*)\.\d{2}\Z", amount):
        return None

    return int(re.sub(r"[\$\.]", "", amount))
