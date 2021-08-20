def get_issuer(n):
    if str(n)[:2] in ['34', '37'] and len(str(n)) == 15:
        return 'AMEX'
    if str(n)[:4] == '6011' and len(str(n)) == 16:
        return 'Discover'
    if str(n)[:2] in ['51', '52', '53', '54', '55'] and len(str(n)) == 16:
        return 'Mastercard'
    if str(n)[:1] == '4' and (len(str(n)) == 13 or len(str(n)) == 16):
        return 'VISA'
    else:
        return 'Unknown'
