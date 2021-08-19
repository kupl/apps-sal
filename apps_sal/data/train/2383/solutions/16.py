for i in range(int(input())):
    (a, b) = list(map(int, input().split()))
    c = max(a, 2 * b)
    c1 = max(b, 2 * a)
    f = min(c, c1)
    print(f * f)
