t = int(input())
for z in range(t):
    n = int(input())
    d = {}
    for i in range(n):
        (k, v) = [int(x) for x in input().split()]
        if k < 9:
            if k not in d:
                d[k] = v
            elif v > d[k]:
                d[k] = v
    if not d:
        print('0')
    else:
        x = d.values()
        x = list(x)
        print(sum(x))
