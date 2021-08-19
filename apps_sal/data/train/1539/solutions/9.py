t = int(input())
while t > 0:
    t -= 1
    c = 0
    j = input()
    s = input()
    n = j.__len__()
    m = s.__len__()
    l = int(m)
    p = int(n)
    for i in range(l):
        for k in range(p):
            if s[i] == j[k]:
                c += 1
                break
    print(c)
