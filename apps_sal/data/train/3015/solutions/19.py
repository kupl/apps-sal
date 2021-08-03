def get_issuer(m):
    m = str(m)
    if int((m)[0:2]) in (34, 37) and len(m) == 15:
        return 'AMEX'
    elif int((m)[0:4]) == 6011 and len(m) == 16:
        return 'Discover'
    elif int((m)[0:2]) in range(50, 56) and len(m) == 16:
        return 'Mastercard'
    elif int((m)[0]) == 4 and len(m) in (13, 16):
        return 'VISA'
    else:
        return 'Unknown'
