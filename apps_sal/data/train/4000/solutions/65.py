def strong_num(number):
    n = 0
    for i in str(number):
        m = 1
        for x in range(1, int(i) + 1):
            m *= x
        n += m
    if number == n:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
