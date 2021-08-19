t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = 0
        for j in range(i + 1, n):
            x ^= l[j]
            if x == l[i]:
                ans += j - i
    print(ans)
