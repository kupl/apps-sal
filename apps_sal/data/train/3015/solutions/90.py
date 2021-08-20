def get_issuer(number):
    num = str(number)
    if num.startswith('34') or (num.startswith('37') and len(num) == 15):
        return 'AMEX'
    elif num.startswith('6011') and len(num) == 16:
        return 'Discover'
    elif num[0] + num[1] in ('51', '52', '53', '54', '55') and len(num) == 16:
        return 'Mastercard'
    elif num[0] == '4' and str(len(num)) in ('13', '16'):
        return 'VISA'
    return 'Unknown'
