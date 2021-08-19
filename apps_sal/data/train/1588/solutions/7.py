from collections import OrderedDict
for _ in range(int(input())):
    a = []
    min = 10000
    n = int(input())
    s = [0] * n
    l = [0] * n
    flag = 0
    for i in range(n):
        (s[i], t) = input().split()
        t = int(t)
        a.append(t)
    l = a.copy()
    a.sort()
    for x in range(len(a)):
        if a.count(a[x]) == 1:
            m = x
            flag = 1
            break
    if flag == 0:
        print('Nobody wins.')
    else:
        h = l.index(a[m])
        print(s[h])
