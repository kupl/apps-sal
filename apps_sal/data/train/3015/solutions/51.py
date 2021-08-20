def get_issuer(number):
    s = str(number)
    if len(s) == 15 and s[:2] in ['34', '37']:
        return 'AMEX'
    if len(s) == 16:
        if s.startswith('6011'):
            return 'Discover'
        if s[:2] in ['51', '52', '53', '54', '55']:
            return 'Mastercard'
    if len(s) in [13, 16] and s[0] == '4':
        return 'VISA'
    return 'Unknown'
