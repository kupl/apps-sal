# cook your dish here
from collections import Counter as cp
t = int(input())
for i in range(t):
    n = int(input())
    p = input().split()
    l = cp(p)
    r = int(n / 2)
    if l.most_common(1)[0][1] <= r:
        print('Yes')
    else:
        print('No')
        continue
    counter_list = []
    t_list = []
    for j in range(n):
        counter_list.append(int(p[j]))
        t_list.append((j, int(p[j])))
    t_list.sort(key=lambda x: x[1])
    # print(t_list)
    for k in range(n):
        q = t_list[k]
        # print(q)
        s = t_list[(k + r) % n]
        # print(s)
        counter_list[q[0]] = s[1]
    for k in range(n - 1):
        print(counter_list[k], end=' ')
    print(counter_list[n - 1])
