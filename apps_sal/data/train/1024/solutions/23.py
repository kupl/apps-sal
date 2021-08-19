T = int(input())
if T >= 1 and T <= 50:
    pos = 0
    imp = 0
    for i in range(0, T):
        (s, n, k, r) = [int(x) for x in input().split()][:4]
        if (n >= 1 and n <= 15) and (s >= 1 and s <= 10000000000) and (k >= 1 and k <= 5) and (r >= 1 and r <= 5):
            total = k
            for j in range(0, n - 1):
                k = k * r
                total = total + k
            mid = s - total
            if total > s:
                imp = imp + abs(mid)
                print('IMPOSSIBLE {}'.format(abs(mid)))
            else:
                pos = pos + abs(mid)
                print('POSSIBLE {}'.format(abs(mid)))
    if pos > imp:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
