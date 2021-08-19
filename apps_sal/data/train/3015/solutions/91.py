def get_issuer(number):
    if str(number)[0:2] == '37' and len(str(number)) == 15 or (str(number)[0:2] == '34' and len(str(number)) == 15):
        return 'AMEX'
    elif str(number)[0:4] == '6011' and len(str(number)) == 16:
        return 'Discover'
    elif str(number)[0:2] == '51' or str(number)[0:2] == '52' or str(number)[0:2] == '53' or (str(number)[0:2] == '54') or (str(number)[0:2] == '55' and len(str(number)) == 16):
        return 'Mastercard'
    elif str(number)[0] == '4' and len(str(number)) == 13:
        return 'VISA'
    elif str(number)[0] == '4' and len(str(number)) == 16:
        return 'VISA'
    else:
        return 'Unknown'
