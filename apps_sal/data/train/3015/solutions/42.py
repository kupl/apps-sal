def get_issuer(n):
    if str(n)[:2] in ('34', '37') and len(str(n)) == 15:
        return 'AMEX'
    if str(n)[:4] == '6011' and len(str(n)) == 16:
        return 'Discover'
    if int(str(n)[:2]) in range(51, 56) and len(str(n)) == 16:
        return 'Mastercard'
    if str(n)[0] == '4' and len(str(n)) in (13, 16):
        return 'VISA'
    return 'Unknown'
