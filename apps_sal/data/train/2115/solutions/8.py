n = input().split()
a = int(n[0])
b = int(n[1])
t = input().split()
c = []
u = 0
if a <= 2:
    print(0)
    return
c.append(int(t[0]))
c.append(int(t[1]))
for i in range(2,a):
    c.append(int(t[i]))
    while c[-1] - c[0] > b:
        del c[0]
        k = len(c) - 1
        u += k * (k - 1) / 2
k = len(c)
u += k * (k - 1) * (k - 2) / 6
print(int(u))

