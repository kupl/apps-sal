def get_issuer(n):
    n = str(n)
    if (n.startswith('34') or n.startswith('37')) and len(n) == 15:
        return 'AMEX'
    elif n.startswith('6011') and len(n) == 16:
        return 'Discover'
    elif 50 < int(n[:2]) < 56 and len(n) == 16:
        return 'Mastercard'
    elif n.startswith('4') and len(n) in [13, 16]:
        return 'VISA'
    return 'Unknown'
