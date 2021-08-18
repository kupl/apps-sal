import math
from math import log10


def score(df):
    n = len(df)

    res = {}
    for val in df:
        for key in val:
            if key not in res:
                res[key] = 1
            else:
                res[key] += 1

    fx = 1
    for val in res.values():
        fx = fx * val

    li2 = {}
    for val in res:
        li2[val] = 0
        for i in df:
            if val in i:
                li2[val] += 1

    x = 1
    for val in li2:

        x = x * li2[val]
    return [x, fx]


def prog(li):
    al = []
    bo = []
    for cur in li:
        prev = -1
        f = 0
        for j in range(len(cur)):
            if cur[j] not in ['a', 'e', 'i', 'o', 'u']:
                if prev == -1:
                    prev = j
                else:
                    if abs(prev - j) == 2 or abs(prev - j) == 1:
                        f = 1
                        break
                    else:
                        prev = j
        if f == 1:
            bo.append(cur)
        else:
            al.append(cur)

    sca = score(al)
    scb = score(bo)
    ans1 = log10(sca[0]) + len(bo) * log10(scb[1])
    ans2 = log10(scb[0]) + len(al) * (log10(sca[1]))
    ans1 = ans1 - ans2

    return ans1


t = int(input())
for i in range(0, t):
    li = []
    x = int(input())
    for i in range(0, x):
        e = input()
        li.append(e)
    final = prog(li)
    if final > 7.0:
        print("Infinity")
    else:
        print(pow(10, final))
