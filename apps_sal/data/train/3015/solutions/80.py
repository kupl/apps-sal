def get_issuer(number):
    n = str(number)
    if n[0:2] == "34" or n[0:2] == "37" and len(n) == 15:
        return "AMEX"
    elif n[0] == "4" and (len(n) == 13 or len(n) == 16):
        return "VISA"
    elif n[0] == "5" and len(n) == 16:
        if 1 <= int(n[1]) <= 5:
            return "Mastercard"
        else:
            return "Unknown"
    elif n[0:4] == "6011" and len(n) == 16:
        return "Discover"
    else:
        return "Unknown"
