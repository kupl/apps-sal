def get_issuer(number):
    try:
        s = str(number)
        if (s.startswith('34') or s.startswith('37')) and len(s) == 15:
            return 'AMEX'
        if s.startswith('6011') and len(s) == 16:
            return 'Discover'
        if int(s[0]) == 5 and int(s[1]) in [1, 2, 3, 4, 5] and (len(s) == 16):
            return 'Mastercard'
        if s.startswith('4') and (len(s) == 13 or len(s) == 16):
            return 'VISA'
        return 'Unknown'
    except:
        return 'Unknown'
