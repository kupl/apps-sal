def get_issuer(number):
    if len(str(number)) == 15 and str(number)[0:2] in ['34', '37']:
        return 'AMEX'
    elif len(str(number)) == 16 and str(number)[0:4] == '6011':
        return 'Discover'
    elif len(str(number)) == 16 and str(number)[0:2] in ['51', '52', '53', '54', '55']:
        return 'Mastercard'
    elif len(str(number)) in [13, 16] and str(number)[0] == '4':
        return 'VISA'
    else:
        return 'Unknown'
