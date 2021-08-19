def get_issuer(number):
    strnumber = str(number)
    print(len(strnumber), strnumber)
    if strnumber[0] == '4':
        if len(strnumber) in [13, 16]:
            return 'VISA'
    elif strnumber[:2] in ['34', '37']:
        if len(strnumber) == 15:
            return 'AMEX'
    elif strnumber[:2] in ['51', '52', '53', '54', '55']:
        if len(strnumber) == 16:
            return 'Mastercard'
    elif strnumber[:4] == '6011':
        if len(strnumber) == 16:
            return 'Discover'
    return 'Unknown'
