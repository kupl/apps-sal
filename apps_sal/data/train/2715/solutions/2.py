def counter_effect(hit):
    b = []
    for i in str(hit):
        a = []
        for k in range(int(i) + 1):
            a.append(k)
        b.append(a)
    return b
