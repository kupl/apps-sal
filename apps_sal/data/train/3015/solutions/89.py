def get_issuer(number):
    number = str(number)

    if number.startswith("4") and (len(number) == 13 or len(number) == 16):
        return "VISA"
    elif number.startswith(("51", "52", "53", "54", "55")) and len(number) == 16:
        return "Mastercard"
    elif number.startswith("6011") and len(number) == 16:
        return "Discover"
    elif number.startswith(("34", "37")) and len(number) == 15:
        return "AMEX"
    else:
        return "Unknown"
