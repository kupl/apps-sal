for _ in range(int(input())):
    (p, i) = map(int, input().split())
    p = 1 << p - 1
    j = 0
    ans = 0
    while p > 0:
        if i >= p:
            ans += 1 << j
            i -= p
        p >>= 1
        j += 1
    print(ans)
