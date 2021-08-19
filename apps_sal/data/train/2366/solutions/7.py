t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s_min = [10 ** 9] * n
    s_min[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        s_min[i] = min(s_min[i + 1], a[i])
    cnt = 0
    for i in range(n - 1):
        cnt += s_min[i + 1] < a[i]
    print(cnt)
