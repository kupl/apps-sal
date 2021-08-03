from math import fabs


def f(x):
    return int(fabs(x - r))


n, r = list(map(int, input().split()))
li = list(map(int, input().split()))
li = list(map(f, li))
for z in range(min(li), 0, -1):
    for k in li:
        if k % z != 0:
            break
    else:
        ans = z
        break
try:
    print(ans)
except Exception:
    print(1)
