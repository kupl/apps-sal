from collections import namedtuple


Issuer = namedtuple('Issuer', 'name, begins, length')

def get_issuer(number):
    issuers = [
        Issuer('AMEX', [34, 37], [15]),
        Issuer('Discover', [6011], [16]),
        Issuer('Mastercard', [51, 52, 53, 54, 55], [16]),
        Issuer('VISA', [4], [13, 16]),
    ]
    number_str = str(number)
    for issuer in issuers:
        if any([number_str.startswith(str(n)) for n in issuer.begins]) and len(number_str) in issuer.length:
            return issuer.name
    return 'Unknown'
