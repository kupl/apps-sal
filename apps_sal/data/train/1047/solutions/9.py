t = int(input())
for _ in range(t):
    n = int(input())
    co = []
    suma = []
    diff = []
    for i in range(n):
        (x, y) = map(int, input().strip().split())
        co.append([x, y])
        suma.append(x + y)
        diff.append(x - y)
    suma.sort()
    diff.sort()
    mina = 10 ** 9
    mina = abs((suma[0] - suma[1]) / 2)
    mina = min(mina, abs((diff[0] - diff[1]) / 2))
    for i in range(1, n - 1):
        mina = min(mina, abs((suma[i] - suma[i + 1]) / 2), abs((diff[i] - diff[i + 1]) / 2))
        if mina == 0.0:
            break
    print(mina)
