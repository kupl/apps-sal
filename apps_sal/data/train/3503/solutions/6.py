def sum_dig_pow(a, b):  # range(a, b) will be studied by the function
    lis = []
    for i in range(a, b + 1):
        temp = str(i)
        su = 0
        for l in range(0, len(temp)):
            su += int(temp[l:l + 1])**(l + 1)
        if su == i:
            lis.append(i)
    return lis
