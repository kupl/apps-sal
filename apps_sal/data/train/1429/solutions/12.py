for _ in range(int(input())):
    n = int(input())
    xl = [int(x) for x in input().split()]
    pl = [float(x) for x in input().split()]
    tl = [0] * 30
    for x, p in zip(xl, pl):
        bs = bin(x)[2:][::-1]
        for i in range(len(bs)):
            if bs[i] == '1':
                tl[i] = (1 - tl[i]) * p + (1 - p) * tl[i]
    ans = 0
    for i in range(30):
        ans += (2**i) * tl[i]
    print(ans)
