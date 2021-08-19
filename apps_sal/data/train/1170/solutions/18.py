result = []
for _ in range(int(input())):
    (N, K) = map(int, input().split())
    distances = list(map(int, input().split()))
    for i in range(N):
        remainder = distances[i] % K
        if remainder == 0:
            x = 1
            result.append(x)
        else:
            y = 0
            result.append(y)
    print(*result, sep='')
    result.clear()
    distances.clear()
