def get_issuer(number):
    b = list(str(number))
    if len(b) < 13:
        return "Unknown"
    elif len(b) > 16:
        return "Unknown"
    elif len(b) == 14:
        return "Unknown"
    elif b[0] == "3":
        if b[1] == "4" or b[1] == "7":
            if len(b) == 15:
                return "AMEX"
            elif len(b) == 13:
                return "Unknown"
        else:
            return "Unknown"
    elif b[0] == "6":
        if b[1] == "0":
            if b[2] == "1":
                if b[3] == "1":
                    if len(b) == 16:
                        return "Discover"
        else:
            return "Unknown"
    elif b[0] == "5":
        if b[1] == "6":
            return "Unknown"
        elif b[1] == "1" or b[1] == "2" or b[1] == "3" or b[1] == "4" or b[1] == "5":
            if len(b) == 16:
                return "Mastercard"
            else:
                return "Unknown"
    elif b[0] == "4":
        if len(b) == 13:
            return "VISA"
        elif len(b) == 16:
            return "VISA"
        else:
            return "Unknown"
    else:
        return "Unknown"
