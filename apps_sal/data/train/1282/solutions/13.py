for _ in range(int(input())):
    (a, b) = map(int, input().split())
    st = bin(a)[2:]
    s = 0
    m = 1
    ans = 0
    for i in range(len(st) - 1, -1, -1):
        if st[i] == '1':
            ans += m * min(m - s, b - a + 1)
            ans %= 1000000007
            s += m
        m *= 2
    print(ans)
