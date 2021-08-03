def get_issuer(number):
  # code your solution here
    if len(str(number)) == 15:
        if str(number)[:2] == "34" or str(number)[:2] == "37":
            res = "AMEX"
        else:
            res = "Unknown"
    elif len(str(number)) == 16:
        l = ["51", "52", "53", "54", "55"]
        if str(number)[:2] in l:
            res = "Mastercard"
        elif str(number)[:4] == "6011":
            res = "Discover"
        elif str(number)[0] == "4":
            res = "VISA"
        else:
            res = "Unknown"
    elif len(str(number)) == 13 and str(number)[0] == "4":
        res = "VISA"
    else:
        res = "Unknown"
    return res
