import re


def get_issuer(number):
    num = str(number)
    if bool(re.match('^3[4|7]\\d{13}$', num)):
        return 'AMEX'
    if bool(re.match('^4(\\d{12}|\\d{15})$', num)):
        return 'VISA'
    if bool(re.match('^5[1-5]\\d{14}$', num)):
        return 'Mastercard'
    if bool(re.match('^6011\\d{12}$', num)):
        return 'Discover'
    return 'Unknown'
