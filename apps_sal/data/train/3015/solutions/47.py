def get_issuer(number):
    issuer = {
        'AMEX':([34,37],[15]),
        'Discover':([6011],[16]),
        'Mastercard':([51,52,53,54,55],[16]),
        'VISA':([4],[13,16])
    }
    for i in issuer:
        for j in issuer[i][0]:
            if str(number).startswith(str(j)) and len(str(number)) in issuer[i][1]: return i
    return 'Unknown'
