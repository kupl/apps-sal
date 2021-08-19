def get_issuer(number):

    def helper(n, x):
        return str(n).startswith(x)
    L = len(str(number))
    if L == 15 and (helper(number, '34') or helper(number, '37')):
        return 'AMEX'
    elif L == 16 and helper(number, '6011'):
        return 'Discover'
    elif L == 16 and max([helper(number, str(i)) for i in range(51, 56)]) == 1:
        return 'Mastercard'
    elif (L == 13 or L == 16) and helper(number, '4'):
        return 'VISA'
    else:
        return 'Unknown'
