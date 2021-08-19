t = int(input())


def power(a, b):
    return a**b


def concatenate(a, b):
    return a + b


def order(arr, i):
    if len(arr) <= 1:
        return arr

    l = []
    r = []
    n = len(arr)
    for j in range(n):
        if arr[j] % power(2, i + 1) < power(2, i):
            l.append(arr[j])
        else:
            r.append(arr[j])
    l = order(l, i + 1)
    r = order(r, i + 1)
    c = concatenate(l, r)
    return c


for _ in range(t):
    p, idx = list(map(int, input().split()))
    n = 2**p - 1
    l = []
    s = 0
    while(p > 0):
        l.append(int(idx % 2))
        idx = idx / 2
        p -= 1
        # print(l)
    for i in l:
        s = s * 2 + i
    print(s)
    t -= 1
