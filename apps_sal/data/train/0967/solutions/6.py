def solve(l, i, n, m):
    if m == 0:
        return 1
    elif i >= n:
        return 0
    elif m < 0:
        return 0
    else:
        return solve(l, i + 1, n, m - l[i]) + solve(l, i + 1, n, m)


T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    l = list(map(int, input().split()))
    print(solve(l, 0, len(l), M))
