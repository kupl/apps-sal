def time_correct(t):
    if t == "":
        return ""
    try:
        if t is None:
            return None
        elif len(t) != 8:
            return None
        else:
            a, b, c = map(int, t.split(':'))
            if c >= 60:
                c -= 60
                b += 1
            if b >= 60:
                b -= 60
                a += 1
            if a >= 24:
                a = a % 24
            return '%02d:%02d:%02d' % (a, b, c)
    except:
        return None
