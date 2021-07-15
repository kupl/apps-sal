N,M = map(int, input().split())
A = list(map(int, input().split()))
L = -1
R = M
while L < R - 1:
    mid = (L + R) // 2
    last = 0
    k = 1
    for i in A:
        if last == i:
            continue
        if last > i:
            if i + mid >= last:
                continue
            else:
                k = 0
                break
        else:
            if i + mid - M >= last:
                continue
            else:
                last = i
    if k == 1:
        R = mid
    else:
        L = mid
print(R)
