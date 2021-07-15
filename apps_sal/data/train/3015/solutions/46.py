def get_issuer(number):
    if (len(str(number)) == 13 or len(str(number)) == 16) and str(number)[0] == '4':
        return 'VISA'
    if len(str(number)) == 15 and (str(number)[:2] == '34' or str(number)[:2] == '37'):
        return 'AMEX'
    if len(str(number)) == 16:
        if str(number)[:4] == '6011':
            return 'Discover'
        if int(str(number)[:2]) in range(51, 56):
            return 'Mastercard'
    return 'Unknown'
