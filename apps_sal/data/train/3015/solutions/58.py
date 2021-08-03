from re import match


def get_issuer(number):
    s = str(number)
    return\
        'AMEX' if match(r'^3[47](\d){13}$', s) else\
        'Discover' if match(r'^6011(\d){12}$', s) else\
        'Mastercard' if match(r'^5[1-5](\d){14}$', s) else\
        'VISA' if match(r'^4((\d){12}|(\d){15})$', s) else\
        'Unknown'
