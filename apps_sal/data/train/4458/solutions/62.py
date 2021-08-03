def time_correct(t):
    if t == '':
        return t
    try:
        t = t.split(':')
        assert(len(t) == 3)
        assert(len(t[1]) == 2)
        assert(len(t[2]) == 2)
        t = list(map(int, t))
        if t[2] > 59:
            t[1], t[2] = t[1] + 1, t[2] - 60
        if t[1] > 59:
            t[0], t[1] = t[0] + 1, t[1] - 60
        t[0] %= 24
        t = ["%02d" % _ for _ in t]
        return ':'.join(t)
    except Exception as e:
        print(e)
