def bs(a, n, k):
    l = 0
    h = n - 1
    while(l <= h):
        mid = (l + h) // 2
        if a[mid] == k:
            return 1
        if a[mid] < k:
            l = mid + 1
        else:
            h = mid - 1
    return 0


t = int(input())
for kk in range(t):
    ntr = int(input())
    tr = [int(x) for x in input().split()]
    tr.sort()
    ndr = int(input())
    dr = [int(x) for x in input(). split()]
    dr.sort()
    nts = int(input())
    ts = [int(x) for x in input().split()]
    nds = int(input())
    ds = [int(x) for x in input().split()]
    s = 1
    for i in range(nts):
        if bs(tr, ntr, ts[i]):
            continue
        else:
            s = 0
            break
    if s == 0:
        print("no")
        continue
    for i in range(nds):
        if bs(dr, ndr, ds[i]):
            continue
        else:
            s = 0
            break
    if s == 0:
        print("no")
        continue
    if s == 1:
        print("yes")
