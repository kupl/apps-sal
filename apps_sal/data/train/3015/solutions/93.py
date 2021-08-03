def get_issuer(number):
    len_ = len(str(number))
    if len_ == 15 and (str(number)[:2] == '34' or str(number)[:2] == '37'):
        return 'AMEX'
    elif len_ == 16 and str(number)[:4] == '6011':
        return 'Discover'
    elif len_ == 16 and str(number)[:2] in ['51', '52', '53', '54', '55']:
        return 'Mastercard'
    elif len_ in [13, 16] and str(number)[:1] == '4':
        return 'VISA'
    else:
        return 'Unknown'
