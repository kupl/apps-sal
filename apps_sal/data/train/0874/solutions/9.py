for _ in range(int(input())):
    (n, m, s) = map(int, input().split())
    ls = list(map(int, input().split()))
    ls.sort()
    ans = 0
    for i in range(n):
        if ls[i] <= s:
            if m > 0:
                ans += 1
                m -= 1
            else:
                break
        elif ls[i] <= 2 * s:
            if m > 1:
                ans += 1
                m -= 2
            else:
                break
        else:
            break
    print(ans)
