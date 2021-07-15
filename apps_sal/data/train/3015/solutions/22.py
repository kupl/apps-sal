def get_issuer(number):
    print(number)
    if len(str(number))<13:
        return 'Unknown'
    elif str(number)[0]=='4' and (len(str(number))==13 or len(str(number))==16):
        return 'VISA'
    elif str(number)[:4]=='6011':
        return 'Discover'
    else:
        return {
        '34':'AMEX',
        '37':'AMEX',
        '51':'Mastercard',
        '52':'Mastercard',
        '53':'Mastercard',
        '54':'Mastercard',
        '55':'Mastercard',
    }.get(str(number)[:2], 'Unknown')

