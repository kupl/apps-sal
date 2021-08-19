def get_issuer(number):
    if str(number)[0] == '3' and str(number)[1] == '4' or (str(number)[1] == '7' and len(str(number)) == 15):
        return 'AMEX'
    elif len(str(number)) == 16 and str(number)[0:4] == '6011':
        return 'Discover'
    elif len(str(number)) == 16 and str(number)[0] == '5' and (str(number)[1] == '1' or str(number)[1] == '2' or str(number)[1] == '3' or (str(number)[1] == '4') or (str(number)[1] == '5')):
        return 'Mastercard'
    elif (len(str(number)) == 13 or len(str(number)) == 16) and str(number)[0] == '4':
        return 'VISA'
    else:
        return 'Unknown'
