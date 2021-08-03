def get_issuer(number):
    if len(str(number)) == 15 and (str(number)).startswith('34'):
        return 'AMEX'
    elif len(str(number)) == 15 and (str(number)).startswith('37'):
        return 'AMEX'
    elif len(str(number)) == 13 and (str(number)).startswith('4'):
        return 'VISA'
    elif len(str(number)) == 16 and (str(number)).startswith('4'):
        return 'VISA'
    elif len(str(number)) == 16 and (str(number)).startswith('6011'):
        return 'Discover'
    elif len(str(number)) == 16 and (str(number)).startswith('51'):
        return 'Mastercard'
    elif len(str(number)) == 16 and (str(number)).startswith('52'):
        return 'Mastercard'
    elif len(str(number)) == 16 and (str(number)).startswith('53'):
        return 'Mastercard'
    elif len(str(number)) == 16 and (str(number)).startswith('54'):
        return 'Mastercard'
    elif len(str(number)) == 16 and (str(number)).startswith('55'):
        return 'Mastercard'
    else:
        return 'Unknown'
