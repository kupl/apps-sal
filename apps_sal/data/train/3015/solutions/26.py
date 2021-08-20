def get_issuer(number):
    if str(number).startswith('34') or (str(number).startswith('37') and len(str(number)) == 15):
        return 'AMEX'
    if str(number).startswith('6011') and len(str(number)) == 16:
        return 'Discover'
    if str(number).startswith('5') and int(str(number)[1]) < 6 and (len(str(number)) == 16):
        return 'Mastercard'
    if str(number).startswith('4') and (len(str(number)) == 13 or len(str(number)) == 16):
        return 'VISA'
    else:
        return 'Unknown'
