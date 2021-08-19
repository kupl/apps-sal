def order(arr, i):
    if len(arr) <= 1:
        return arr
    l = arr[::2]
    r = arr[1::2]
    l = order(l, i + 1)
    r = order(r, i + 1)
    c = l + r
    return c


t = int(input())
while t > 0:
    (p, idx) = list(map(int, input().split()))
    a = []
    sizeinp = pow(2, p) - 1
    for i in range(sizeinp + 1):
        a.append(i)
    print(order(a, 0)[idx])
    t -= 1
