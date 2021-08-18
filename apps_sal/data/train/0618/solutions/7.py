for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x = x[-(k):] + x
    y = sum(x[0:k])
    z = sum(x[0:k])
    for i in range(k, len(x)):
        z = (z - x[i - k]) + x[i]
        y = max(y, z)
    print(y)
