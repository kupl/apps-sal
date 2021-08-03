def strong_num(number):
    c = 0
    f = 1
    num = str(number)
    for i in num:
        i = int(i)
        for e in range(1, i + 1):
            f = f * e
        c = c + f
        f = 1
    if c == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
