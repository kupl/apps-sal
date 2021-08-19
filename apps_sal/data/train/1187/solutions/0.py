for _ in range(int(input())):
    (N, M) = list(map(int, input().split()))
    (count, e, perm) = (0, 0, 1)
    while True:
        (lim, start) = (N // M ** e, N // M ** (e + 1) + 1)
        num = lim - start + 1
        divs = num // M
        if start + divs * M <= lim:
            r = (start + divs * M) % M
            if r == 0 or r + (lim - (start + divs * M)) >= M:
                divs += 1
        cmon = num - divs
        if e % 2 == 0:
            count += cmon * ((e + 2) // 2)
        else:
            count += cmon * (e // 2 + 1)
            perm = perm * pow((e + 3) // 2, cmon, 998244353) % 998244353
        e += 1
        if start == 1:
            break
    print(count, perm)
