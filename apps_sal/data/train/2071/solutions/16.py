n = int(input())


def inx(x, d):
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
    return d


def input2(n):
    dx = {}
    dy = {}
    dob = {}
    ans = 1
    for i in range(n):
        x, y = map(int, input().split())
        dx = inx(x, dx)
        dy = inx(y, dy)
        if (x, y) in dob:
            dob[(x, y)] += 1
        else:
            dob[(x, y)] = 1
    return dx, dy, dob


dx, dy, dob = input2(n)


def ans(d):
    ans1 = 0
    for i in d:
        ans1 += d[i] * (d[i] - 1) // 2
    return ans1


myans = ans(dx) + ans(dy) - ans(dob)
print(myans)
