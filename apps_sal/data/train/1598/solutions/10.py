t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    avg = 0
    for i in range(n):
        (x, p, m) = input().split(' ')
        p = int(p)
        m = int(m)
        avg += m
        l.append([x, p, m])
    avg = avg // n
    ret = []
    for i in range(n):
        if l[i][2] <= avg:
            ret.append([l[i][0], l[i][1], l[i][2]])
    ret.sort()
    for i in range(len(ret)):
        print(ret[i][0], ret[i][1], ret[i][2])
