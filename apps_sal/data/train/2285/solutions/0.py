for __ in range(int(input())):
    n = int(input())
    s = list(map(int, input()))
    r = [0] * n
    for i in range(10):
        left_lim = 0
        for (j, c) in enumerate(s):
            if c < i:
                left_lim = j + 1
        prv = [-1, -1, -1]
        flg = True
        for (j, c) in enumerate(s):
            r[j] = 1 if c < i or (c == i and j >= left_lim) else 2
            if c < prv[r[j]]:
                flg = False
                break
            prv[r[j]] = c
        if flg:
            print(''.join(map(str, r)))
            break
    if not flg:
        print('-')
