def get_issuer(number):
    number = str(number)
    if (len(number) == 13):
        if(number[0] == '4'):
            return 'VISA'
        else:
            return 'Unknown'
    elif (len(number) == 15):
        if(number[0:2] == '34' or number[0:2] == '37'):
            return 'AMEX'
        else:
            return 'Unknown'
    elif (len(number) == 16):
        if(number[0] == '4'):
            return 'VISA'
        elif(number[0:4] == '6011'):
            return 'Discover'
        elif(number[0:2] == '51' or number[0:2] == '52' or
                number[0:2] == '53' or number[0:2] == '54' or
                number[0:2] == '55'):
            return 'Mastercard'
        else:
            return 'Unknown'
    else:
        return 'Unknown'
