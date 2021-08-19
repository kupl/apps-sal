t = int(input())
while t > 0:
    t = t - 1
    (a, d, l, r) = list(map(int, input().split()))
    s = 0
    p = a + (l - 1) * d
    for i in range(0, r - l + 1):
        if 1 <= l <= r:
            if p < 9:
                q = p
            else:
                q = (p - 1) % 9 + 1
            s = s + q
            p = p + d
    print(s)
