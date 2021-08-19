def lsb(i):
    return bool(i & 1 << 0)


t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    res = []
    for i in m:
        result = lsb(i)
        if result:
            continue
        else:
            res.append(i)
    print(sum(res))
