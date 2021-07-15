def get_issuer(number):
    number = str(number)
    if len(number) == 15 and number.startswith(('34','37')): return 'AMEX'
    elif len(number) == 16 and number.startswith('6011'): return 'Discover'
    elif len(number) == 16 and number.startswith(('51','52','53','54','55')): return 'Mastercard'
    elif len(number) == 16 and number.startswith('4'): return 'VISA'
    elif len(number) == 13 and number.startswith('4'): return 'VISA'
    else: return 'Unknown'
