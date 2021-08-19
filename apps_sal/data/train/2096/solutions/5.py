n = int(input())
a = list(map(int, input().split()))
a = sorted([(a[i], i) for i in range(n)])
b = []
c = [True] * n
for i in range(n):
    if c[i]:
        j = i
        d = []
        while c[j]:
            c[j] = False
            d.append(j + 1)
            j = a[j][1]
        b.append(d)
print(len(b))
for i in b:
    print(len(i), *i)
