def order(arr):
    if len(arr) <= 1:
        return arr
    l = arr[::2]
    r = arr[1::2]
    l = order(l)
    r = order(r)
    c = l + r
    return c


for _ in range(int(input())):
    (p, idx) = list(map(int, input().split()))
    seq = list(range(2 ** p))
    print(order(seq)[idx])
