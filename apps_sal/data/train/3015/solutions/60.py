def get_issuer(n):
    (n, siz) = (str(n), len(str(n)))
    if siz == 15 and n.startswith(('34', '37')):
        return 'AMEX'
    if siz == 16 and n.startswith('6011'):
        return 'Discover'
    if siz == 16 and n.startswith(('51', '52', '53', '54', '55')):
        return 'Mastercard'
    if (siz == 16 or siz == 13) and n.startswith('4'):
        return 'VISA'
    return 'Unknown'
