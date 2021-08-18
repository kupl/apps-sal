for t in range(int(input())):
    a, b, c = map(int, input().split())
    p = (c // a) * a + b
    if p <= c:
        print(p)
    else:
        print(((c // a) - 1) * a + b)
