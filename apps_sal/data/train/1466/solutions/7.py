a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
c = [0]
d = 0
for e in range(a[0]):
    d = d ^ b[e]
    c.append(d)
for j in range(a[1]):
    e = int(input())
    if e <= a[0]:
        print(c[e])
    else:
        print(c[(e - (a[0] + 1)) % (a[0] + 1)])
