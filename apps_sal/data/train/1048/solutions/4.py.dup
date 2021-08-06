for _ in range(int(input())):
    a, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l.sort()
    ans = 0

    s = l[0] - a / 2 - k
    e = l[0] + a / 2 + k

    s = max(s, l[1] - a / 2 - k)
    e = min(e, l[1] + a / 2 + k)

    s = max(s, l[2] - a / 2 - k)
    e = min(e, l[2] + a / 2 + k)

    if s < e:
        ans = min(e - s, a) * a

    print(ans)
