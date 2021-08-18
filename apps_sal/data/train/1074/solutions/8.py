a = int(input())
for i in range(a):
    t = int(input())
    l = list(map(int, input().split()))
    l2 = []
    for j in l:
        if j not in l2:
            l2.append(j)
    l3 = []
    for k in l2:
        l3.append(l.count(k))
    c = 0
    for j in l3:
        c1 = j
        if c1 >= 2:
            while(c1 >= 2):
                c += 1
                c1 = c1 - 2
    print(round(c / 2))
