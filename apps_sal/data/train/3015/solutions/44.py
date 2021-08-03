def get_issuer(number):
    n = str(number)
    if len(n) == 16 and n[:4] == '6011':
        return 'Discover'
    elif n[0] == '4' and len(n) in [13, 16]:
        return 'VISA'
    elif n[0:2] in ['34', '37'] and len(n) == 15:
        return 'AMEX'
    elif int(n[0:2]) in range(51, 56) and len(n) == 16:
        return 'Mastercard'
    else:
        return 'Unknown'
