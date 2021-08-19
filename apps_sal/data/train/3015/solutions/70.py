def get_issuer(number):
    s = str(number)
    if int(s[0:2]) in (34, 37) and len(s) == 15:
        return 'AMEX'
    elif int(s[0:4]) == 6011 and len(s) == 16:
        return 'Discover'
    elif int(s[0:2]) in (51, 52, 53, 54, 55) and len(s) == 16:
        return 'Mastercard'
    elif int(s[0]) == 4 and len(s) in (13, 16):
        return 'VISA'
    return 'Unknown'
