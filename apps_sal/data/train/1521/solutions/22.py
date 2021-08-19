t = int(input())
for _ in range(t):
    n = int(input())
    lower = []
    upper = []
    for __ in range(n):
        (x, y) = map(int, input().split())
        lower.append([x, __])
        upper.append([y, __])
    lower.sort(key=lambda x: x[0], reverse=True)
    upper.sort(key=lambda x: x[0])
    dell = [0] * n
    for i in range(n):
        dell[upper[i][1]] += i
        dell[lower[i][1]] += i
    print(*dell)
