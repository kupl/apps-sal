L = []
l = []

x = int(input())
for i in range(x):
    y = input()
    z = y.split()
    a = z[0]
    b = z[1]
    L.append(a)
    l.append(b)
for j in range(x):
    c = int(L[j]) + int(l[j])
    print(c)
