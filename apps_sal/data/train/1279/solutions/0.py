# cook your dish here
for _ in range(int(input())):
    d = dict()
    ls = []
    for i in range(int(input())):
        ls = list(map(int, input().split()))
        if ls[0] in d:
            d[ls[0]] = max(ls[1], d[ls[0]])
        else:
            d[ls[0]] = ls[1]
    # print(d)
    if len(d) < 3:
        print(0)
    else:
        kd = list(d.values())
        kd.sort()
        # print(kd)
        print(kd[-1] + kd[-2] + kd[-3])
