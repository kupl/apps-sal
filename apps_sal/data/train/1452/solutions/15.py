n = list(map(int, input().split()))
g = []
l = []
for i in range(n[0]):
    m = []
    l = list(map(int, input().split()))
    for j in range(l[1] + 1, l[0] + 1):
        m.append(j)
    for j in range(1, l[1] + 1):
        m.append(j)
    c = 0
    f = 0
    d = {}
    for j in range(0, len(m)):
        if f not in d:
            d[f] = "No"
        if d[f] == "Yes":
            break
        else:
            d[f] = "Yes"
            f = m[f] - 1
        c = c + 1
    if c == len(m):
        g.append("Yes")
    else:
        g.append("No" + " " + str(c))
for i in range(len(g)):
    print(g[i])
