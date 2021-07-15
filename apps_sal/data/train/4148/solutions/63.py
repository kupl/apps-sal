def sum_digits(number):
    sn = str(number)
    rez=0
    for i in sn:
        if i.isnumeric():
            rez+=int(i)
    return rez
