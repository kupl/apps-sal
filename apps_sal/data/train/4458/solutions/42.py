def time_correct(t):
    print(t)
    if t is not None:
        if not t:
            return ''
        t = t.split(':')
        if sum((1 for x in t if x.isdigit() and len(x) == 2)) == 3:
            out = []
            to_add = 0
            for (i, v) in enumerate(t[::-1]):
                v = int(v) + to_add
                if i < 2:
                    to_add = v // 60
                    out.append(('0' + str(v % 60))[-2:])
                else:
                    out.append(('0' + str(v % 24))[-2:])
            return ':'.join(out[::-1])
