#
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))


def check(a, x, m):
    Max = m
    flg = True

    for val in a[::-1]:
        if val <= Max:
            Max = min(Max, val + x)
        else:
            if (val + x) < m:
                flg = False
                break
            else:
                Max = min(Max, (val + x) % m)
    return flg


l = -1
u = m
while u - l > 1:
    md = (u + l) // 2
    if check(a, md, m) == True:
        u = md
    else:
        l = md
print(u)
