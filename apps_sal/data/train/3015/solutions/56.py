import re
def get_issuer(number):
    snum = str(number)
    if len(snum) == 15 and re.search ('^3(4|7)', snum) != None:
        return 'AMEX'
    if len(snum) == 16 and re.search ('^6011', snum) != None:
        return 'Discover'
    if len(snum) == 16 and re.search ('^5([1-5])', snum) != None:
        return 'Mastercard'
    if (len(snum) == 13 or len(snum) == 16) and re.search ('^4', snum) != None:
        return 'VISA'
    return 'Unknown'
