import re

def signed_eight_bit_number(n):
    return bool(re.fullmatch(r"-?(1[01]\d|12[0-7]|[1-9]\d)|-(128|[1-9])|\d", n))

