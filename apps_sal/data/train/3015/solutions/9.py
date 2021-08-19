def get_issuer(n):
    n = str(n)
    if n[:1] == '4' and (len(n) == 13 or len(n) == 16):
        return 'VISA'
    if (n[:2] == '34' or n[:2] == '37') and len(n) == 15:
        return 'AMEX'
    if n[:4] == '6011' and len(n) == 16:
        return 'Discover'
    if n[:1] == '5' and int(n[1]) < 6 and (len(n) == 16):
        return 'Mastercard'
    return 'Unknown'
