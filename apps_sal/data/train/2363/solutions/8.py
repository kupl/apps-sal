T = int(input())
for t in range(T):
    N = int(input())
    strengths = list(map(int, input().split()))
    s = sorted(strengths)

    res = 100000000
    for i in range(N - 1):
        diff = s[i + 1] - s[i]
        res = min(res, diff)

    print(res)

