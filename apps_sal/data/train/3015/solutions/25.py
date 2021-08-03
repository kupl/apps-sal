def get_issuer(number):
    s = str(number)
    if s.startswith('34') or s.startswith('37') and len(s) == 15:
        return 'AMEX'
    if s.startswith('6011') and len(s) == 16:
        return 'Discover'
    if int(s[:2]) in range(51, 56) and len(s) == 16:
        return 'Mastercard'
    if s.startswith('4') and (len(s) == 13 or len(s) == 16):
        return 'VISA'
    return 'Unknown'
