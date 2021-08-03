def get_issuer(number):
    if str(number).startswith('34') or str(number).startswith('37') and len(str(number)) == 15:
        return 'AMEX'
    elif str(number).startswith('51') or str(number).startswith('52') or str(number).startswith('53') or str(number).startswith('54') or str(number).startswith('55'):
        if len(str(number)) == 16:
            return 'Mastercard'
        else:
            return 'Unknown'
    elif str(number).startswith('4'):
        if len(str(number)) == 13 or len(str(number)) == 16:
            return 'VISA'
        else:
            return 'Unknown'
    elif str(number).startswith('6011') and len(str(number)) == 16:
        return 'Discover'
    else:
        return 'Unknown'
