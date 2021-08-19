for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(map(int, input().split()))
    m = max(a)
    mi = a.index(m)
    dp = [0] * (n + 1)
    dp[mi] = 1
    for i in range(mi, -1, -1):
        for j in s:
            if i + j > n:
                continue
            if not dp[i + j]:
                dp[i] = 1
                break
    print('Chef' if dp[0] else 'Garry')
