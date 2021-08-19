def ortho(n, m):
    res = set()
    tot = n * (n + 1) // 2
    pre = {0}
    for x in m:
        pre = {x | y for y in pre} | {x}
        res |= pre
    if len(res) == tot:
        return 'YES'
    return 'NO'


t = int(input())
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(ortho(n, m))
