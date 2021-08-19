# cook your dish here
import sys
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    f = int(input())
    idxs = []
    i = 0
    while i < n - 1:
        if a[i] <= f:
            idxs.append(i)
        i += 1
    if len(idxs) == 0:
        print("impossible")
        continue
    mn = 1000000000
    for k in idxs:
        left = k
        pts = 0
        elm = left - 1
        right = n - 1 - left
        last = n - 2
        sub = a[elm]
        sleft = 1
        slast = 1
        while left > 0:
            if left % 2 == 0:
                elm -= sleft
                sub = a[elm]
                left = left // 2
                sleft *= 2
            else:
                pts += a[elm]
                left = (left + 1) // 2
                sleft *= 2

            if right % 2 == 0:
                last -= slast
                right //= 2
                slast *= 2
            else:
                slast *= 2
                left -= 1
                right = (right + 1) // 2

        while right > 2:
            if right % 2 == 0:
                last -= slast
                sub = a[last]
                right = right // 2
                slast *= 2
            else:
                slast *= 2
                sub = a[last]
                pts += sub
                right = (right + 1) // 2
        if mn > pts:
            mn = pts
            idx = k
            if pts == 0:
                break
    print("possible")
    print(idx + 1, mn + f)
