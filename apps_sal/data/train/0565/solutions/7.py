for _ in range(int(input())):
    (n, q) = list(map(int, input().split()))
    l = [int(i) for i in input().split()]
    d = {}
    ind = {}
    for i in range(n):
        ind[l[i]] = i
    dup = sorted(l)
    for i in range(n):
        chote = i
        bade = n - i - 1
        d[dup[i]] = [chote, bade]
    for _ in range(q):
        chotewale_swap = 0
        badewale_swap = 0
        x = int(input())
        d1 = {}
        d1[0] = d[x][0]
        d1[1] = d[x][1]
        f = 1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if ind[x] == mid:
                break
            elif ind[x] > mid and x > l[mid]:
                d1[0] -= 1
                low = mid + 1
            elif ind[x] > mid and x < l[mid]:
                if d1[0] == 0:
                    f = -1
                    break
                d1[0] -= 1
                chotewale_swap += 1
                low = mid + 1
            elif ind[x] < mid and x < l[mid]:
                d1[1] -= 1
                high = mid - 1
            elif ind[x] < mid and x > l[mid]:
                if d1[1] == 0:
                    f = -1
                    break
                d1[1] -= 1
                badewale_swap += 1
                high = mid - 1
        if f == -1:
            print(-1)
        else:
            print(max(chotewale_swap, badewale_swap))
