def get_issuer(number):
    num = str(number)
    if len(num) == 15 and num.startswith(("34", "37")):
        return "AMEX"
    elif len(num) == 16 and num.startswith("6011"):
        return "Discover"
    elif len(num) == 16 and num.startswith(("51", "52", "53", "54", "55")):
        return "Mastercard"
    elif (len(num) == 13 or len(num) == 16) and num.startswith("4"):
        return "VISA"
    return "Unknown"
