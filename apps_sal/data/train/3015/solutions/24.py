def get_issuer(number):

    number = [int(x) for x in str(number)]
    length = len(number)

    if number[0] == 4 and length == 13 or number[0] == 4 and length == 16:
        return "VISA"
    elif (number[0] == 3 and number[1] == 4) or (number[0] == 3 and number[1] == 7) and length == 15:
        return "AMEX"
    elif number[0] == 5 and (number[1] == 1 or number[1] == 2 or number[1] == 3 or number[1] == 4 or number[1] == 5) and length == 16:
        return "Mastercard"
    elif number[0] == 6 and number[1] == 0 and number[2] == 1 and number[3] == 1 and length == 16:
        return "Discover"
    else:
        return "Unknown"
