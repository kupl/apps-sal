from itertools import combinations
t = int(input())


def pair(arr):
    maxi = 0
    k = 0
    d = 0
    if len(set(arr)) == 1:
        return '{:.8f}'.format(1)
    c = list(combinations(arr, 2))
    for i in c:
        if sum(i) > maxi:
            maxi = sum(i)
        d += 1
    for i in c:
        if sum(i) == maxi:
            k += 1
    p = k / d
    return '{:.8f}'.format(p)


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    r = pair(arr)
    print(r)
