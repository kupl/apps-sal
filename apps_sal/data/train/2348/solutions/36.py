from bisect import *
n = int(input())
x = list(map(int, input().split()))
l = int(input())
q = int(input())
dp_plus = [[0] * (n + 1) for i in range(30)]
dp_minus = [[0] * (n + 1) for i in range(30)]
for i in range(n):
    now = x[i]
    reach = now + l
    dp_plus[0][i + 1] = bisect_right(x, reach)
for i in range(n):
    now = x[i]
    reach = now - l
    dp_minus[0][i + 1] = bisect_left(x, reach) + 1
for i in range(29):
    for j in range(1, n + 1):
        dp_plus[i + 1][j] = dp_plus[i][dp_plus[i][j]]
        dp_minus[i + 1][j] = dp_minus[i][dp_minus[i][j]]
for _ in range(q):
    (a, b) = list(map(int, input().split()))
    ans = 1
    if a < b:
        for i in range(29, -1, -1):
            if dp_plus[i][a] < b:
                a = dp_plus[i][a]
                ans += pow(2, i)
    else:
        for i in range(29, -1, -1):
            if dp_minus[i][a] > b:
                a = dp_minus[i][a]
                ans += pow(2, i)
    print(ans)
