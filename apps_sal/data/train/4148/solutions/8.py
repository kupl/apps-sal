def sum_digits(number):
    inp = str(number)
    s = 0
    for x in inp:
        try:
            s += int(x)
        except:
            pass
    return s
