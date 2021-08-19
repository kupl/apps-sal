import math
t = int(input())
for i in range(t):
    (n, k) = map(int, input().strip().split(' '))
    a = [int(x) for x in input().split()]
    od_a = []
    ev_a = []
    for j in range(n):
        if j % 2 == 0:
            ev_a.append(a[j])
        else:
            od_a.append(a[j])
    ev_a.sort()
    od_a.sort()
    n1 = len(ev_a)
    n2 = len(od_a)
    s1 = sum(ev_a)
    s2 = sum(od_a)
    if s2 > s1:
        print('YES')
        continue
    elif k == 0:
        print('NO')
        continue
    for j in range(k):
        if j == n2:
            break
        if ev_a[n1 - 1 - j] > od_a[j]:
            temp = ev_a[n1 - 1 - j]
            ev_a[n1 - 1 - j] = od_a[j]
            od_a[j] = temp
        s1 -= od_a[j] - ev_a[n1 - 1 - j]
        s2 += od_a[j] - ev_a[n1 - 1 - j]
        if s2 > s1:
            print('YES')
            break
    if s1 >= s2:
        print('NO')
