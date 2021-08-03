from decimal import Decimal
from itertools import cycle


def encode(message, key):
    key_digits = cycle(Decimal(key).as_tuple().digits)
    return [ord(c.lower()) - ord('a') + next(key_digits) + 1 for c in message]
