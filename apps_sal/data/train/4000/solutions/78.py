def strong_num(number):
    str_num = list(str(number))
    a = 0
    for i in str_num:
        f = 1
        j = int(i)
        if j != 0:
            for k in range(1, (j + 1)):
                f *= k
        a += f
    if a == number:
        return "STRONG!!!!"
    return "Not Strong !!"
