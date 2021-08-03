def get_issuer(number):
    n = str(number)
    if n[0] == '4' and (len(n) == 16 or len(n) == 13):
        return 'VISA'
    if n[0] == '5' and n[1] in '12345' and len(n) == 16:
        return "Mastercard"
    if n[0:4] == '6011' and len(n) == 16:
        return "Discover"
    if n[0] == '3' and n[1] in '47' and len(n) == 15:
        return 'AMEX'
    return 'Unknown'
