def get_issuer(number):
    if str(number).startswith('6011') and len(str(number))==16:
        return 'Discover'
    elif str(number).startswith(('34','37')) and len(str(number))==15:
        return 'AMEX'
    elif str(number).startswith(('51','52','53','54','55')) and len(str(number))==16:
        return 'Mastercard'
    elif str(number).startswith('4') and (len(str(number))==16 or len(str(number))==13):
        return 'VISA'
    else:
        return 'Unknown'
