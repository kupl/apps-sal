def get_issuer(number):
    card = str(number)
    if len(card) == 15 and card[:2] in ('34', '37'):
        return 'AMEX'
    elif len(card) == 16 and card.startswith('6011'):
        return 'Discover'
    elif len(card) == 16 and card[:2] in ('51', '52', '53', '54', '55'):
        return 'Mastercard'
    elif len(card) in (13, 16) and card[0] == '4':
        return 'VISA'
    return 'Unknown'
