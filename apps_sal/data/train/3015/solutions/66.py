def get_issuer(number: int):
    number = str(number)
    if number[:2] in ('34', '37') and len(number) == 15:
        return 'AMEX'
    elif number[:4] == '6011' and len(number) == 16:
        return 'Discover'
    elif number[:2] in ('51', '52', '53', '54', '55') and len(number) == 16:
        return 'Mastercard'
    elif number[0] == '4' and len(number) in (13, 16):
        return 'VISA'
    return 'Unknown'
