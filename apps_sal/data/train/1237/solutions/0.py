for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    p = a * 100 + b
    mx = p
    ans, cnt = 0, 0
    while True:
        cnt += 1
        if p < c or cnt == 10000:
            break

        else:
            p -= c
            a = p // 100
            b = p % 100
            p = b * 100 + a
            if p > mx:
                mx = p
                ans = cnt

    print(ans)
