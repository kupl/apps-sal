def get_issuer(number):
    x = str(number)
    return 'AMEX' if x[:2] in ('34', '37') and len(x) == 15 else 'Discover' if x[:4] == '6011' and len(x) == 16 else 'Mastercard' if x[:2] in ('51', '52', '53', '54', '55') and len(x) == 16 else 'VISA' if x[0] == '4' and len(x) in (13, 16) else 'Unknown'
