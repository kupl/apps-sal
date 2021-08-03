def get_issuer(number):
    nb_str = str(number)
    l = len(nb_str)

    if l == 13:
        return "VISA" if nb_str[0] == "4" else "Unknown"
    if l == 15:
        return "AMEX" if nb_str[:2] in ["34", "37"] else "Unknown"
    if l != 16:
        return "Unknown"
    if nb_str[:4] == "6011":
        return "Discover"
    if nb_str[0] == "4":
        return "VISA"
    if nb_str[0] == "5" and nb_str[1] in "12345":
        return "Mastercard"
    return "Unknown"
