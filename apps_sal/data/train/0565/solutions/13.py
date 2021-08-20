t = int(input())
while t > 0:
    t -= 1
    (n, q) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    tarr = sorted(arr)
    d = {}
    inddir = {}
    for i in range(len(arr)):
        inddir[arr[i]] = i
    tarrlen = len(tarr)
    for i in range(len(tarr)):
        d[tarr[i]] = [i, tarrlen - i - 1]
    for _ in range(q):
        k = int(input())
        find = inddir[k]
        (l, r) = (1, tarrlen)
        gs = 0
        ls = 0
        sw = 0
        tempc = d[k].copy()
        while l <= r:
            mid = (l + r) // 2
            if mid - 1 == find:
                break
            elif mid - 1 < find:
                if arr[mid - 1] < k:
                    if tempc[0] > 0:
                        tempc[0] -= 1
                    else:
                        sw = -1
                        break
                elif tempc[0] > 0:
                    tempc[0] -= 1
                    sw += 1
                    ls += 1
                else:
                    sw = -1
                    break
                l = mid + 1
            else:
                if arr[mid - 1] > k:
                    if tempc[1] > 0:
                        tempc[1] -= 1
                    else:
                        sw = -1
                        break
                elif tempc[1] > 0:
                    tempc[1] -= 1
                    sw += 1
                    gs += 1
                else:
                    sw = -1
                    break
                r = mid - 1
        print(max(ls, gs) if sw != -1 else -1)
