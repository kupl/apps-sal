for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans, cur_max, cur, count = 0, [a, b], 0, 10000
    while count > 0 and (b >= c or a > 0):
        cur += 1
        count -= 1
        if b < c:
            b += 100
            a -= 1

        b -= c
        if cur_max < [b, a]:
            ans = cur
            cur_max = [b, a]
        a, b = b, a
    print(ans)
