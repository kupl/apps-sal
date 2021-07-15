def get_issuer(number):
    n = str(number)
    return ["Unknown", "AMEX", "Discover", "Mastercard", "VISA"][(len(n) == 15 and n[:2] in ["34", "37"]) + 2 * (len(n) == 16 and n[:4] == "6011") + 3 * (len(n) == 16 and n[:2] in ["51", "52", "53", "54", "55"]) + 4 * (len(n) in [13, 16] and n[0] == "4")]
