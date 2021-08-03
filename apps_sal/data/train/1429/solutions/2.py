for _ in range(int(input())):
    n = int(input())
    B = [int(x) for x in input().split()]
    P = [float(x) for x in input().split()]
    tl = [0] * 30
    for b, p in zip(B, P):
        bs = bin(b)[2:][::-1]
        for i in range(len(bs)):
            if bs[i] == '1':
                tl[29 - i] = (1 - tl[29 - i]) * p + (1 - p) * tl[29 - i]
    ans = 0
    for i in range(29, -1, -1):
        ans += (2**(29 - i)) * tl[i]
    print(ans)
