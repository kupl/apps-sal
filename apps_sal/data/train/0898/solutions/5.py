def solve(y):
    res = len(str(y))
    if y < int(str(9) * res):
        res -= 1
    return res


t = int(input())
for _ in range(t):
    (m, n) = map(int, input().split())
    x = m
    print(x * solve(n), x)
