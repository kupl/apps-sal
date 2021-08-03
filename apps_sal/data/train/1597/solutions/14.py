t = int(input())
for i in range(t):
    am = input().split()
    a = int(am[0])
    m = int(am[1])
    l = list()
    c = 0
    indx = m // a
    for i in range(indx, 0, -1):
        diff = m - i * a
        if(diff > i):
            break
        if(diff != 0):
            if(i % diff == 0):
                c += 1
                l.append(i)
    l.sort()
    res = str()
    for i in range(len(l)):
        res = res + str(l[i]) + " "
    res.rstrip()
    print(c)
    print(res)
