n = int(input())
for _ in range(n):
    s = input()
    (l, r, u, d) = [s.count(i) for i in 'LRUD']
    lr = min(l, r)
    ud = min(u, d)
    res = ''
    if lr == 0 and ud == 0:
        res = ''
    elif lr == 0:
        res = 'UD'
    elif ud == 0:
        res = 'LR'
    else:
        res = 'R' * lr + 'U' * ud + 'L' * lr + 'D' * ud
    print(len(res))
    print(res)
