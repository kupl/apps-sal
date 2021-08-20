def find_num(n):
    l = [0]
    while len(l) <= n:
        m = 1
        while m in l or any([x in str(l[-1]) for x in str(m)]):
            m += 1
        l.append(m)
    return l[n]
