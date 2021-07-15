for i in range(int(input())):
    l, r = map(int, input().split())
    if l == r: print(l)
    else:
        k = len(bin(l ^ r)) - 2
        s = ((r >> k) + 1 << k) - 1
        if s > r: s -= 1 << k - 1
        print(s)
