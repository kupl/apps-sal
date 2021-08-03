def get_issuer(number):
    number = str(number)
    if (number[0:2] == "34" or number[0:2] == "37") and len(number) == 15:
        return "AMEX"
    elif number[0:4] == "6011" and len(number) == 16:
        return "Discover"
    elif (number[0:2] == "51" or number[0:2] == "52" or number[0:2] == "53" or number[0:2] == "54" or number[0:2] == "55") and len(number) == 16:
        return "Mastercard"
    elif number[0:1] == "4" and (len(number) == 13 or len(number) == 16):
        return "VISA"
    else:
        return "Unknown"
