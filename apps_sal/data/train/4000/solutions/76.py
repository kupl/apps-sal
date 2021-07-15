def strong_num(number):
    ln = [int(x) for x in str(number)]
    ln = [1 if x == 0 else x for x in ln]
    f = 1
    ff = []
    fff = []
    for d in ln:
        for x in range(1, d + 1):
            f *= x
            ff.append(f)
        fff.append(ff[-1])
        f = 1
    if number == int(sum(fff)):
        return 'STRONG!!!!'
    return 'Not Strong !!'
    # Flez

