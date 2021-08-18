for _ in range(int(input())):
    c = 0
    x, y, n = tuple(map(int, input().split()))
    for z in range(0, n + 1):
        if x ^ z < y ^ z:
            c += 1
    print(c)
