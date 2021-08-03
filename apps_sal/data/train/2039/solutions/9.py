n, m = list(map(int, input().split()))
a = [int(i) for i in input().split()]
L = -1
R = m
while L < R - 1:
    mid = (L + R) // 2
    last = 0
    isok = True
    for el in a:
        if last == el:
            continue
        if last > el:
            if el + mid >= last:
                continue
            else:
                isok = False
                break
        else:
            if el + mid - m >= last:
                continue
            else:
                last = el
    if isok:
        R = mid
    else:
        L = mid
print(R)
