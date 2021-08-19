def get_issuer(number):
    number = str(number)
    if len(number) == 15 and number[:2] in ('34', '37'):
        return 'AMEX'
    if len(number) == 16 and number[:4] == '6011':
        return 'Discover'
    if len(number) == 16 and '51' <= number[:2] <= '55':
        return 'Mastercard'
    if len(number) in (13, 16) and number[0] == '4':
        return 'VISA'
    else:
        return 'Unknown'
