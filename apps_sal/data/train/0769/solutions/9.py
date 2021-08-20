def hcf(x, y):
    if y == 0:
        return x
    else:
        return hcf(y, x % y)


i = int(input())
for j in range(i):
    m = input()
    m = m.split()
    a = int(m[0])
    b = int(m[1])
    if a >= b:
        print(hcf(a, b))
    else:
        print(hcf(b, a))
