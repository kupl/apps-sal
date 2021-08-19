def div_con(x):
    num = 0
    strnum = 0
    for number in x:
        if int(number) == number:
            num = num + number
        else:
            strnum = strnum + int(number)
    num = num - strnum
    return num
