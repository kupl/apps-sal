def get_issuer(number):
    n = str(number)
    if len(n) == 15 and n[:2] == '34' or n[:2] =='37': return 'AMEX'
    elif len(n) == 16 and n[:4] == '6011': return 'Discover'
    elif len(n) == 16 and int(n[:2]) in range(51,56): return 'Mastercard'
    elif len(n) in [13,16] and n[0] == '4': return 'VISA'
    else: return 'Unknown'
