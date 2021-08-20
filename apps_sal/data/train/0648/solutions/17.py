import sys
ar = list(map(int, input().strip().split(' ')))
n = ar[0]
q = ar[1]
gre = []
for i1 in range(n + 2):
    gre.append(0)
n1 = list(map(int, input().strip().split(' ')))
n1.insert(0, 0)
for i1 in range(q):
    a = list(map(int, input().strip().split(' ')))
    if a[0] == 2:
        l = a[1]
        r = a[2]
        x = a[3]
        gre[l] += x
        gre[r + 1] -= x
    elif a[0] == 1:
        i = a[1]
        k = a[2]
        g = gre[i]
        w1 = i
        m1 = n1[i] + g
        for qw in range(i + 1, n + 1):
            g += gre[qw]
            if qw - w1 > 100:
                break
            if k == 0:
                break
            if n1[qw] + g > m1:
                m1 = n1[qw] + g
                w1 = qw
                k = k - 1
        print(w1)
