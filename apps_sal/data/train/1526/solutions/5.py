import math


def score(df):
    res, fx, li2, x = {}, 1, {}, 1
    for val in df:
        for key in val:
            if key not in res:
                res[key] = 1
            else:
                res[key] += 1
    for val in res.values():
        fx = fx * val
    for val in res:
        li2[val] = 0
        for i in df:
            if val in i:
                li2[val] += 1
    for val in li2:
        x *= li2[val]
    return [x, fx]


def prog(li, al, bo):
    for cur in li:
        prev, f = -1, 0
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
    sca, scb = score(al), score(bo)
    ans1 = math.log10(sca[0]) + len(bo) * math.log10(scb[1])
    ans2 = math.log10(scb[0]) + len(al) * (math.log10(sca[1]))
    return (ans1 - ans2)


for i in range(int(input())):
    li, x = [], int(input())
    for i in range(x):
        li.append(input())
    final = prog(li, [], [])
    print("Infinity") if final > 7.0 else print(pow(10, final))
