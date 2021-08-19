def get_issuer(number):
    number = number // 1000000000000
    if number == 4:
        return 'VISA'
    if number == 6011:
        return 'Discover'
    number = number // 10
    if number == 34 or number == 37:
        return 'AMEX'
    if 50 < number // 10 < 56:
        return 'Mastercard'
    if number // 100 == 4:
        return 'VISA'
    return 'Unknown'
