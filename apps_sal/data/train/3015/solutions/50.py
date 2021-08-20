import re


def get_issuer(number):
    print(number)
    if re.search('^3(4|7)\\d{13}\\Z', str(number)):
        return 'AMEX'
    if re.search('^6011\\d{12}\\Z', str(number)):
        return 'Discover'
    if re.search('^5[1-5]\\d{14}\\Z', str(number)) != None:
        return 'Mastercard'
    if re.search('^4(\\d{12}|\\d{15})\\Z', str(number)):
        return 'VISA'
    return 'Unknown'
