def get_issuer(number):
    if str(number)[0: 2] in ["34", "37"] and len(str(number)) == 15:
        return "AMEX"
    elif str(number)[0] == "4" and len(str(number)) in [13, 16]:
        return "VISA"
    elif str(number)[0: 2] in ["51", "52", "53", "54", "55"] and len(str(number)) == 16:
        return "Mastercard"
    elif str(number)[0: 4] == "6011" and len(str(number)) == 16:
        return "Discover"
    else:
        return "Unknown"
