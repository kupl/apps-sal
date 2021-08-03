n = int(input())
b = 0
li = []
for i in range(n):
    g = input()
    h = input()
    for z in g:
        if z in li:
            continue
        li.append(z)
        if h.count(z) == 0:
            continue
        elif h.count(z) == g.count(z):
            b += h.count(z)
        elif h.count(z) != g.count(z):
            b += min(h.count(z), g.count(z))
    print(b)
    b = 0
    li.clear()
