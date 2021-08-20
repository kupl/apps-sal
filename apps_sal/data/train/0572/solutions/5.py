for _ in range(int(input())):
    (a, m, g) = [int(x) for x in input().split()]
    r = abs(a - m)
    if g <= r:
        print(r - g)
    else:
        print(0)
