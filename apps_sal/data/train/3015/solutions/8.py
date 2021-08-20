from re import match


def get_issuer(number):
    number = str(number)
    if match('^3[4|7]\\d{13}$', number):
        return 'AMEX'
    if match('^6011\\d{12}$', number):
        return 'Discover'
    if match('^5[1-5]\\d{14}$', number):
        return 'Mastercard'
    if match('^4(\\d{12}|\\d{15})$', number):
        return 'VISA'
    return 'Unknown'
