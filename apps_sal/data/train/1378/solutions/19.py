def __starting_point():
    (a, n, k) = list(map(int, input().split()))
    (s, i) = ([], 0)
    if n == 0:
        print(*[0] * k)
    else:
        while a > 0:
            s.append(a % (n + 1))
            a = a // (n + 1)
            i += 1
        s = s + [0] * (k - i)
        if len(s) <= k:
            print(*s)
        else:
            print(*s[:k])


__starting_point()
