for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    ab = bin(a)[2:]
    bb = bin(b)[2:]
    n = abs(len(bb) - len(ab))
    if n > 0:
        if len(bb) > len(ab):
            ab = '0' * n + ab
        else:
            bb = '0' * n + bb
    m = 0
    count = 0
    for i in range(len(bb)):
        l = int(ab, 2) ^ int(bb, 2)
        if l > m:
            m = l
            count = i
        bb = bb[-1] + bb
        bb = bb[:-1]
    print(count, m)
