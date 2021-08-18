n = int(input())
y = []
for i in range(0, n):
    l = []
    s = input()
    l = s.split(":")
    l[0] = int(l[0])
    l[1] = int(l[1])
    if l[0] >= 12:
        l[0] = l[0] - 12
    l[1] = l[1] // 5
    m, e = 1, 1
    r = 0
    if l[0] < l[1]:
        m = m * l[1] * 2.5
        e = (l[1] - l[0]) * 30 * e
        r = e - m
    elif l[0] > l[1]:
        m = m * l[1] * 2.5
        e = (l[0] - l[1]) * 30 * e
        r = m + e
    else:
        m = m * l[1] * 2.5
        r = m
    if r > 180:
        r = 360 - r
    y.append(r)
for j in y:
    print("{0:.2f}".format(j).rstrip('0').rstrip('.'), "degree")
