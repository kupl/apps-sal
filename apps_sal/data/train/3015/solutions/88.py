def get_issuer(number):
    if len(str(number)) == 15 and int(str(number)[:2]) == 34 or int(str(number)[:2]) == 37:
        return "AMEX"
    elif len(str(number)) == 16 and int(str(number)[:4]) == 6011:
        return "Discover"
    elif len(str(number)) == 16 and int(str(number)[:2]) == 51 or len(str(number)) == 16 and int(str(number)[:2]) == 52 or len(str(number)) == 16 and int(str(number)[:2]) == 53 or len(str(number)) == 16 and int(str(number)[:2]) == 54 or len(str(number)) == 16 and int(str(number)[:2]) == 55:
        return "Mastercard"
    elif int(str(number)[:1]) == 4 and len(str(number)) == 13 or int(str(number)[:1]) == 4 and len(str(number)) == 16:
        return "VISA"
    else:
        return "Unknown"
