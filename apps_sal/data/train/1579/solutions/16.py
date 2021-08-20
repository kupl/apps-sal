t = int(input())
while t != 0:
    n = int(input())
    ls = list(map(int, input().split()))
    p = {0}
    res = set()
    for i in ls:
        p = {i | y for y in p} | {i}
        res |= p
    if len(res) == n * (n + 1) // 2:
        print('YES')
    else:
        print('NO')
    t -= 1
