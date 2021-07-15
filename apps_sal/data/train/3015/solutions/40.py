def get_issuer(a):
    n=str(a)
    if n.startswith('34') or n.startswith('37') and len(n)==15:
        return 'AMEX'
    elif n.startswith('6011') and len(n)==16:
        return 'Discover'
    elif n.startswith('51') or n.startswith('52') or n.startswith('53') or n.startswith('54') or n.startswith('55') and len(n)==16:
        return 'Mastercard'
    elif n.startswith('4') and len(n)==13 or n.startswith('4') and len(n)==16:
        return 'VISA'
    else:
        return 'Unknown'
