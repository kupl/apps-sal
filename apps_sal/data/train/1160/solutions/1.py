import math


def CHAHG1(xh, m):
    x = [x for x in xh]
    y = [y for y in m]

    up = []
    lw = []
    L = None
    R = None
    for i in range(0, len(x) - 1):
        if(i % 2 == 0):
            if((y[i] - y[i + 1]) == 0):
                if(x[i] < x[i + 1]):
                    lw.append(0)
                else:
                    return False
            else:
                if(y[i] < y[i + 1]):
                    l = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    l = int(math.floor(l)) + 1
                    lw.append(max(0, l))
                else:
                    r = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    r = int(math.ceil(r)) - 1
                    if(r < 0):
                        return False
                    up.append(r)
        else:
            if((y[i] - y[i + 1]) == 0):
                if(x[i] > x[i + 1]):
                    lw.append(0)
                else:
                    return False
            else:
                if(y[i] > y[i + 1]):
                    l = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    l = int(math.floor(l)) + 1
                    lw.append(max(0, l))
                else:
                    r = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    r = int(math.ceil(r)) - 1
                    if(r < 0):
                        return False
                    up.append(r)
    if(len(lw) > 0):
        L = max(lw)
    else:
        L = 0
    if(len(up) > 0):
        R = min(up)
        if(L > R):
            return False
    else:
        R = "Inf"

    return L, R


def CHAHG2(xh, m):
    x = [x for x in xh]
    y = [y for y in m]
    up = []
    lw = []
    L = None
    R = None
    for i in range(0, len(x) - 1):
        if(i % 2 == 1):
            if((y[i] - y[i + 1]) == 0):
                if(x[i] < x[i + 1]):
                    lw.append(0)
                else:
                    return False
            else:
                if(y[i] < y[i + 1]):
                    l = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    l = int(math.floor(l)) + 1
                    lw.append(max(0, l))
                else:
                    r = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    r = int(math.ceil(r)) - 1
                    if(r < 0):
                        return False
                    up.append(r)
        else:
            if((y[i] - y[i + 1]) == 0):
                if(x[i] > x[i + 1]):
                    lw.append(0)
                else:
                    return False
            else:
                if(y[i] > y[i + 1]):
                    l = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    l = int(math.floor(l)) + 1
                    lw.append(max(0, l))
                else:
                    r = (float)(x[i + 1] - x[i]) / (y[i] - y[i + 1])
                    r = int(math.ceil(r)) - 1
                    if(r < 0):
                        return False
                    up.append(r)
    if(len(lw) > 0):
        L = max(lw)
    else:
        L = 0
    if(len(up) > 0):
        R = min(up)
        if(L > R):
            return False
    else:
        R = "Inf"

    return L, R


T = int(input())
while T:
    T = T - 1
    N = int(input())
    xh = []
    m = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        xh.append(a)
        m.append(b)

    res = []
    p = CHAHG1(xh, m)
    q = CHAHG2(xh, m)
    if(p is not False):
        res.append(p)
    if(q is not False):
        res.append(q)

    res.sort()
    sz = len(res)

    if(N == 1):
        print("1")
        print("0 Inf")
    else:
        if(sz == 2 and (res[0][1] + 1 == res[1][0])):
            print("1")
            print(res[0][0], res[1][1])
        else:
            print(sz)
            for L, R in res:
                print(L, R)
