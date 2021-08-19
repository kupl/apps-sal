from re import match


def get_issuer(number):
    s = str(number)
    return 'AMEX' if match('^3[47](\\d){13}$', s) else 'Discover' if match('^6011(\\d){12}$', s) else 'Mastercard' if match('^5[1-5](\\d){14}$', s) else 'VISA' if match('^4(\\d){12}$', s) or match('^4(\\d){15}$', s) else 'Unknown'
