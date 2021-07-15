def get_issuer(number):
    num = str(number)
    if (num[:2] == '34' or num[:2] == '37') and len(num) == 15:
        return 'AMEX'
    elif num[:4] == '6011' and len(num) == 16:
        return 'Discover'
    elif num[:2] in ['51', '52', '53', '54','55'] and len(num) == 16:
        return 'Mastercard'
    elif num[:1] == '4' and (len(num) == 16 or len(num) == 13):
        return 'VISA'
    return 'Unknown'

