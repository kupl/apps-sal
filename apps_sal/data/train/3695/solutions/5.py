def repeat_adjacent(string):
    a = list(string)
    b = []
    if len(a) >= 2:
        if a[1] ==a[0]:
            b.append(1)
        for i in range(2, len(a)):
            if a[i-1] == a[i] and a[i-1] != a[i-2]:
                b.append(1)
            elif a[i-1] != a[i]:
                b.append(0)
        c = []
        if b[0] == 1:
            c.append(1)
        for i in range(1, len(b)):
            if b[i] == 1:
                c.append(1)
            else:
                if b[i-1] == 0:
                    c.append(0)
        k = 0
        for i in range(1, len(c)-1):
            if c[i] == 1 == c[i-1] and c[i+1] == 0:
                k += 1
        if c[len(c)-1] == 1 == c[len(c)-2]:
            k += 1
    else:
        k = 0
    return k
