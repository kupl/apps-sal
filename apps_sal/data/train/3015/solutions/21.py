def get_issuer(number):
    if int(str(number)[:2]) in (34, 37) and len(str(number)) == 15:
        return 'AMEX'
    elif int(str(number)[:4]) == 6011 and len(str(number)) == 16:
        return 'Discover'
    elif 51 <= int(str(number)[:2]) <= 55 and len(str(number)) == 16:
        return 'Mastercard'
    elif int(str(number)[0]) == 4 and len(str(number)) in (13, 16):
        return 'VISA'
    return 'Unknown'
