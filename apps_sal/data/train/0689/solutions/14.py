a = []
b = []
c = 0
for _ in range(int(input())):
    (x, y) = list(map(int, input().split()))
    z = x + y
    a.append(z)
    b.append(x)
for i in range(len(a)):
    z = a[i]
    z1 = b[i]
    for j in range(len(a)):
        if j != i:
            z2 = a[j]
            z3 = b[j]
            if z == z3 and z1 == z2:
                c = 1
                break
if c == 1:
    print('YES')
else:
    print('NO')
