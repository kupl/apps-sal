q = int(input())
for it in range(q):
    a, b = list(map(int, input().split()))
    if a * b <= 2:
        print((0))
        continue
    lo, hi = 1, a*b - 1
    while lo < hi:
        x = (lo + hi + 1) // 2
        #l = list(range(max(1, x // 2 - 2), x // 2 + 3))
        #r = list(range(max(1, x // 2 - 2), x // 2 + 3))
        if x % 2 == 0:
            r1, r2 = x // 2, x // 2 + 1
            l1, l2 = x // 2, x // 2 + 1
        else:
            l, r = (x + 1) // 2, (x + 1) // 2 
            if a <= l:
                l += 1
            if b <= r:
                r += 1
            if l * r < a * b:
                lo = x
            else:
                hi = x - 1
            continue
        if b <= r1:
            r1 += 1
            r2 += 1
        #elif b >= r2 and b <= x:
        #    r1 -= 1
        #    r2 -= 1
        if a <= l1:
            l1 += 1
            l2 += 1
        #elif a >= l2 and a <= x:
        #    l1 -= 1
        #    l2 -= 1
        if l1 * r2 < a*b and l2 * r1 < a*b:
            lo = x
        else:
            hi = x - 1
    print(lo)

