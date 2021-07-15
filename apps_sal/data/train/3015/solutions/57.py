def get_issuer(number):
    import re
    try:
        groups = re.match(r'((?:34|37)\d{13})|(6011\d{12})|(5[1-5]\d{14})|(4(?:\d{12}|\d{15})$)', str(number)).groups()
    except AttributeError:
        return 'Unknown'
    if groups[0] is not None:
        return 'AMEX'
    elif groups[1] is not None:
        return 'Discover'
    elif groups[2] is not None:
        return 'Mastercard'
    elif groups[3] is not None:
        return 'VISA'
