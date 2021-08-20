from math import log


def get_issuer(number):
    length = int(log(number, 10) + 1)
    (first_one, first_two, first_four) = (number // 10 ** (length - 1), number // 10 ** (length - 2), number // 10 ** (length - 4))
    if length == 16:
        if first_one == 4:
            return 'VISA'
        if first_two in range(51, 56):
            return 'Mastercard'
        if first_four == 6011:
            return 'Discover'
    elif length == 15:
        if first_two in (34, 37):
            return 'AMEX'
    elif length == 13:
        if first_one == 4:
            return 'VISA'
    return 'Unknown'
