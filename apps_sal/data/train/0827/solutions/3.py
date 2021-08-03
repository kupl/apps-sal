for _ in range(int(input())):
    n, k = map(int, input().split())
    s = [x for x in input().strip()]
    c1 = s.count('a')
    c2 = s.count('b')
    ans = 0
    m = 0
    for x in s:
        if x == 'b':
            m += 1
        if x == 'a':
            ans += (((k * (k + 1)) // 2) * c2) - (k * m)
    print(ans)
