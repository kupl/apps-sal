for _ in range(int(input())):

    l = list(map(int, input().split()))
    l.sort()

    print((l[0] * (l[1] - 1) * (l[2] - 2)) % 1000000007)
