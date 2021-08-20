def get_issuer(number):
    s = str(number)
    l = len(s)
    return {s[:2] in ('34', '37') and l == 15: 'AMEX', s[:4] == '6011' and l == 16: 'Discover', s[:2] in ('51', '52', '53', '54', '55') and l == 16: 'Mastercard', s[0] == '4' and (l == 13 or l == 16): 'VISA'}.get(True, 'Unknown')
