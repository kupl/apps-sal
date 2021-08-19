for _ in range(int(input())):
    (x, y, n) = list(map(int, input().split()))
    c = 0
    for i in range(n + 1):
        if x ^ i < y ^ i:
            c += 1
    print(c)
