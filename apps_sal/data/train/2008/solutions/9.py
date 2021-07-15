from math import ceil

def __starting_point():
    n = int(input())
    arr = list(map(int, input().split()))

    narr = [True]

    for i in range(1, n - 1):
        x = arr[i]
        narr.append(x == arr[i - 1] or x == arr[i + 1])

    narr.append(True)

    cnt = 0
    mc = 0

    for x in narr:
        if not x:
            cnt += 1
        if x and cnt:
            mc = max(mc, cnt)
            cnt = 0

    if cnt:
        mc = max(mc, cnt)

    print(ceil(mc / 2))

    ss = None

    for i, x in enumerate(arr):
        if not narr[i]:
            if ss is None:
                ss = i
        elif ss is not None:
            if arr[ss - 1] == x:
                for j in range(ss, i):
                    arr[j] = x
            else:
                for j in range(ss, i):
                    arr[j] = arr[ss - 1] if j < (i + ss) / 2 else x
            ss = None

    print(*arr)

__starting_point()
