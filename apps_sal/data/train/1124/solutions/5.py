for _ in range(int(input())):

    n, p, q = list(map(int, input().split()))

    l = sorted(map(int, input().split()))
    ans = 0
    for amount in l:
        check = 0
        while amount > 0:

            if q > 0 and amount >= 2:
                amount -= 2
                q -= 1
            elif p > 0:
                amount -= 1
                p -= 1
            if p == 0 and q == 0:
                break

        if amount == 0:
            ans += 1

        if p == 0 and q == 0:
            break

    print(ans)
