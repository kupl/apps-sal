for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    (p, q, r) = map(int, input().split())
    if p < a or q < b or r < c:
        print(-1)
    else:
        ans = 0
        if p > a:
            ans += p - a
        if q > b:
            ans += q - b
        if r > c:
            ans += r - c
        print(ans)
