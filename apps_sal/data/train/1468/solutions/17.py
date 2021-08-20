t = int(input())
for i in range(t):
    h = list(reversed(list(input())))
    v = 'ABCDEF'
    r = [10, 11, 12, 13, 14, 15]
    x = 0
    for j in range(len(h)):
        if h[j] not in v:
            x = x + int(h[j]) * 16 ** j
        else:
            y = r[v.index(h[j])]
            x = x + int(y) * 16 ** j
    print(x)
