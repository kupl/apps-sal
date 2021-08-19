def get_issuer(number):
    if str(number).startswith('4') and len(str(number)) in (13, 16):
        return 'VISA'
    elif str(number).startswith('6011') and len(str(number)) == 16:
        return 'Discover'
    elif int(str(number)[0:2]) in list(range(51, 56)) and len(str(number)) == 16:
        return 'Mastercard'
    elif int(str(number)[0:2]) in (34, 37) and len(str(number)) == 15:
        return 'AMEX'
    else:
        return 'Unknown'
