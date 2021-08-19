def get_issuer(number):
    str_num = str(number)
    if (str_num[0:2] == '34' or str_num[0:2] == '37') and len(str_num) == 15:
        return 'AMEX'
    elif str_num[0:4] == '6011' and len(str_num) == 16:
        return 'Discover'
    elif (str_num[0] == '5' and int(str_num[1]) <= 5) and len(str_num) == 16:
        return 'Mastercard'
    elif str_num[0] == '4' and (len(str_num) == 13 or len(str_num) == 16):
        return 'VISA'
    else:
        return 'Unknown'
