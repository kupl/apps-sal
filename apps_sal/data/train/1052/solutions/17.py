def dsum(n):
    ddsum = 0
    while(n != 0):
        a = int(n % 10)
        ddsum = ddsum + a
        n = int(n / 10)
    return ddsum


for _ in range(0, int(input())):
    l = []
    a, b = map(int, input().split())
    minval = 1000000000
    val = a
    cnt = 0
    inv = 0
    l.append([])
    l[inv].append(val)
    l[inv].append(cnt)
    if(minval > val):
        minval = val
        fcnf = cnt
    for j in range(0, 50000):
        q = l.pop(0)
        inv -= 1
        l.append([])
        cnt = q[1] + 1
        inv += 1
        l[inv].append(q[0] + b)
        l[inv].append(cnt)
        if(minval > (q[0] + b)):
            minval = (q[0] + b)
            fcnf = cnt
        # print(l)
        if(q[0] > 9):
            p = dsum(q[0])
            l.append([])
            inv += 1
            l[inv].append(p)
            l[inv].append(cnt)
            if(minval > p):
                minval = p
                fcnf = cnt
    print(minval, fcnf)
