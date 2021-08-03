n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    m = a
    bits = str(a).count('1')
    x = 0
    while a <= b:
        a |= (1 << x)
        z = bin(a).count('1')
        if z > bits and a <= b:
            m = a
            bits = z
        elif z == bits and a < m:
            m = a
        x += 1
    print(m)
