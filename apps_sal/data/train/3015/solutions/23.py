def get_issuer(number):
    card_str = str(number)
    master_card_prefix = list(range(51, 56))
    if card_str[0] == '4':
        if len(card_str) == 13 or len(card_str) == 16:
            return 'VISA'
        else:
            return 'Unknown'
    elif card_str[0:2] == '34' or card_str[0:2] == '37':
        if len(card_str) == 15:
            return 'AMEX'
        else:
            return 'Unknown'
    elif card_str[0:4] == '6011':
        if len(card_str) == 16:
            return 'Discover'
        else:
            return 'Unknown'
    elif int(card_str[0:2]) in master_card_prefix:
        if len(card_str) == 16:
            return 'Mastercard'
        else:
            return 'Unknown'
    else:
        return 'Unknown'
