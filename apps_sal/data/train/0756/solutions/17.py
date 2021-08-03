def factors(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c


t = int(input())
for _ in range(t):
    z = 1
    x, y = map(int, input().split(" "))
    k = x + y
    while(True):
        t = k + z
        if factors(t) == 2:
            break
        else:
            z += 1
    print(z)
    t -= 1
