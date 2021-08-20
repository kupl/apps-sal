for _ in range(int(input())):
    (n, k) = list(map(int, input().split(' ')))
    s = input().split(' ')
    try:
        a = list(map(int, s))
    except:
        a = list(map(int, s[:-1]))
    out = -1
    dp = [a[0]]
    for i in range(1, k):
        dp.append(dp[-1] + a[i])
        out = max(out, dp[-1])
    i = k
    visited = False
    while True:
        dp.append(dp[-1] - a[(i - k) % n] + a[i])
        out = max(out, dp[-1])
        if i == n - 1:
            if not visited:
                visited = True
            else:
                break
        i = (i + 1) % n
    print(out)
