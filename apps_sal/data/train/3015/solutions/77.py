def get_issuer(n):
    if str(n)[:2] in ['34','37'] and len(str(n)) == 15:
        return 'AMEX'
    elif str(n)[:2] in ['51','52','53','54','55'] and len(str(n)) == 16:
        return 'Mastercard'
    elif str(n)[0] == '4' and len(str(n)) in (13,16):
        return 'VISA'
    elif str(n)[:4] == '6011' and len(str(n)) == 16:
        return 'Discover'
    else:
        return 'Unknown'
