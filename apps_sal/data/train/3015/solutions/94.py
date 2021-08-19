def get_issuer(number):
    n = str(number)
    length = len(n)
    if int(n[:2]) in [34, 37] and length == 15:
        return 'AMEX'
    elif n.startswith('6011') and length == 16:
        return 'Discover'
    elif int(n[:2]) in range(51, 56) and length == 16:
        return 'Mastercard'
    elif n[0] == '4' and (length == 13 or length == 16):
        return 'VISA'
    return 'Unknown'
