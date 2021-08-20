for _ in range(int(input())):
    r = [int(x) for x in input().split()]
    (a, b, c) = sorted(r)
    print(a * (b - 1) * (c - 2) % 1000000007)
