from math import ceil


def within(l, k, h):
    s = 0
    for i in range(len(l)):
        t = ceil(l[i] / k)
        s += t
    if s <= h:
        return True
    else:
        return False


for _ in range(int(input())):
    n, h = map(int, input().split())
    l = list(map(int, input().split()))
    l_1 = 1
    r_1 = max(l)
    while l_1 != r_1:
        mid = l_1 + ((r_1 - l_1) // 2)
        if within(l, mid, h) == True:
            r_1 = mid
        else:
            l_1 = mid + 1
    print(l_1)
