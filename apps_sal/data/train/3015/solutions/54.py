def get_issuer(number):
    # code your solution here
    n = str(number)
    m = len(n)
    if n[:2] in ("34", "37") and m == 15:
        return "AMEX"
    if n[:4] in ("6011") and m == 16:
        return "Discover"
    if n[:2] in ("51", "52", "53", "54", "55") and m == 16:
        return "Mastercard"
    if n[:1] in ("4") and m in (13, 16):
        return "VISA"
    else:
        return "Unknown"
