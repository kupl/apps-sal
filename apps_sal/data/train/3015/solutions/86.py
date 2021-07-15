def get_issuer(number):
    kard = str(number)
    
    if kard[0] == '4' and (len(kard)== 16 or len(kard) == 13):
        return "VISA"
    elif kard[0:4] == '6011'and len(kard)==16:
        return "Discover"
    elif kard[0:2] == '34' or kard[0:2] == '37' and len(kard)==15:
        return "AMEX"
    elif kard[0:2] == '51' or kard[0:2] == '52' or kard[0:2] == '53' or kard[0:2] == '54' or kard[0:2] == '55' and len(kard)== 16:
        return "Mastercard"
    else:
        return "Unknown"

