t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    m = 0

    for i in range(n):
        s, p, v = list(map(int, input().split(" ")))
        z = p // (s + 1)
        z *= v
        if z > m:
            m = z
    print(m)
