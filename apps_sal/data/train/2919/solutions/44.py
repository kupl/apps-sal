def encode(m, k):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    count = 0
    l = []
    p = []
    n = []
    st = str(k)
    lst = list(st)
    for x in range(len(m)):
        num = d.get(m[x])
        l.append(num)
    while count < len(l):
        for y in range(len(lst)):
            if count < len(l):
                p.append(int(lst[y]))
                count = count + 1
            else:
                break
    for z in range(len(l)):
        calc = l[z] + p[z]
        n.append(calc)
    return n
