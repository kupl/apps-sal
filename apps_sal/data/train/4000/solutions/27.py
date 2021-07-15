def strong_num(number):
    o = 0
    s = 0
    strong = 'STRONG!!!!'
    nstrong = 'Not Strong !!'
    for i in str(number):
        o = 1
        while int(i) > 0:
            o *= int(i)
            i = int(i) - 1
        s = s + o
    if number == s:
        return strong
    else:
        return nstrong
