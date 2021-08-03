def get_issuer(n):
    print(str(n))
    if str(n)[0] == "4" and (len(str(n)) == 13 or len(str(n)) == 16):
        return "VISA"
    if str(n)[0:4] == "6011" and len(str(n)) == 16:
        return "Discover"
    if str(n)[0] == "5" and str(n)[1] in "12345" and len(str(n)) == 16:
        return "Mastercard"
    if str(n)[0:2] == "34" or str(n)[0:2] == "37":
        return "AMEX"
    else:
        return 'Unknown'
