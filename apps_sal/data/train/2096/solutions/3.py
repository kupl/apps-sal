import sys
n = int(input())
a = list(map(int, input().split()))
a = sorted([(a[i], i) for i in range(n)])
d = []
c = [False] * n
for i in range(n):
    if not c[i]:
        k = i
        p = []
        while not c[k]:
            c[k] = True
            p.append(str(k + 1))
            k = a[k][1]
        d.append(p)
print(len(d))
for i in d:
    print(str(len(i)) + ' ' + ' '.join(i))
