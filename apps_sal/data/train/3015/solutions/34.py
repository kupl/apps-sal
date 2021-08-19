def get_issuer(number):
    if str(number)[0] == '4':
        if len(str(number)) == 13 or len(str(number)) == 16:
            return 'VISA'
    if str(number)[0:2] in ['51', '52', '53', '54', '55'] and len(str(number)) == 16:
        return 'Mastercard'
    if str(number)[0:4] == '6011' and len(str(number)) == 16:
        return 'Discover'
    if str(number)[0:2] in ['34', '37'] and len(str(number)) == 15:
        return 'AMEX'
    return 'Unknown'
