def create_phone_number(n):
    d = '('
    for i in range(len(n)):
        if i < 3:
            d = d + str(n[i])
            if i == 2:
                d = d + ') '
        elif i >= 3 and i < 6:

            d = d + str(n[i])
            if i == 5:
                d = d + '-'
        elif i >= 6 and i < 10:

            d = d + str(n[i])
    return d
