def get_issuer(n):
    n = str(n)
    if len(n) == 15 and n[:2] in ('34', '37'):
        return 'AMEX'
    if len(n) == 16 and n[:4] == '6011':
        return 'Discover'
    if len(n) == 16 and n[:2] in ('51', '52', '53', '54', '55'):
        return 'Mastercard'
    if len(n) in (13, 16) and n[0] == '4':
        return 'VISA'
    return 'Unknown'
