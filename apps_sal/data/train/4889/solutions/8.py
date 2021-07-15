def max_hexagon_beam(n: int,ll: tuple):
# n = 5
# l1 = [4,3,8,7,5,1]
    l1 = list(ll)
    tn = (n * ((2*n)-1)) + (((2*n)-n-1)**2)
    mid = (2*n-1)
    nest = [0 for i in range(mid)]
    for i in range (0, n):
        nest[n-i-1] = mid-i
        nest[n+i-1] = mid-i
    xv = l1[:tn%len(l1)]
    l2 = [l1*(tn//len(l1))+xv]
    cnt = 0
    a0 = [[]]*len(nest)
    a1 = [[0] * mid] * mid
    a2 = [[0] * mid] * mid
    for st in range (0, len(nest)):
        a0[st] = l2[0][cnt:cnt+nest[st]]
        cnt += nest[st]
    for st in range (0,n):
        a1[st] = a0[st] + [0]*(mid-nest[st])
        a1[mid-1-st] = [0]*(mid-nest[st]) + a0[mid-st-1]
        a2[st] = [0]*(mid-nest[st]) + a0[st]
        a2[mid-1-st] = a0[mid-st-1] + [0]*(mid-nest[st]) 
    sm0 = [0]*mid
    sm1 = [0]*mid
    sm2 = [0]*mid
    for i in range (0, mid):
        for j in range (0, mid):
            sm1[j] += a1[i][j]
            sm2[j] += a2[i][j]
    for i in range (0, mid):
        sm0[i] = sum(a0[i])
    return (max(sm0+sm1+sm2))

