def get_issuer(number):
    card = str(number)
    nums = len(card)
    if card[:2] in ('34', '37') and nums == 15:
        return 'AMEX'
    elif card[:4] == '6011' and nums == 16:
        return 'Discover'
    elif 51 <= int(card[:2]) <= 55 and nums == 16:
        return 'Mastercard'
    elif card[0] == '4' and nums in (13, 16):
        return 'VISA'
    return 'Unknown'
