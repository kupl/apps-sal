def R(): return list(map(int, input().split()))


sum1 = 0
p1 = 1
a = [0] * 263000
b = a
n, r = R()
p1 = 2**n
a = R()
sum1 = sum(a)
p2 = sum1 / p1
for i in range(r):
    z, g = R()
    sum1 = sum1 - a[z] + g
    a[z] = g
    b[i] = sum1 / p1
print(p2)
for i in range(r):
    print(b[i])
