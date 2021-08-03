def func(l):
    a = sum(l) // len(l)
    al = [a]
    for q in [2, 8, 16]:
        s, te = al[0], []
        for i in range(0, 20):
            if s > (q - 1):
                te.append(str(s % q))
                s = s // q
            else:
                te.append(str(s))
                break
        if q != 16:
            al.append(''.join(x for x in te[::-1]))
        else:
            d = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}
            al.append(''.join(d.get(x) if int(x) > 9 else x for x in te[::-1]))
    return al
