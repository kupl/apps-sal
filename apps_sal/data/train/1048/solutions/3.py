# cook your dish here
for _ in range(int(input())):

    l, k = map(float, input().split())
    x = sorted(list(map(float, input().split())))
    a, b, c = x[0], x[1], x[2]
    if c - a <= l:
        d = c - a
        if d <= 2 * k:
            print(l * l)
        else:
            d = l - (c - a) + 2 * k
            print(min(abs(d), l) * l)

    else:
        d = 2 * k - (c - a - l)
        if d <= 0:
            print(0.0000000000000000000000000)
        else:
            print(min(l, d) * l)
