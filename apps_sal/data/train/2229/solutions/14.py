t = input()
p = input()

a = list(map(int, input().strip().split()))
a = [ x - 1 for x in a]
n = len(t)
m = len(p)


lo = 0
hi = n - 1

while lo < hi:
    mid = (lo + hi) >> 1
    
    temp = list(t)
    for x in a[ :mid+1]:
        temp[x] = '_'
    
    ptr, curr = 0, 0
    while ptr < n and curr < m:
        while ptr < n and temp[ptr] != p[curr]:
            ptr += 1
        if ptr < n:
            ptr += 1
            curr += 1
    
    if curr == m:
        lo = mid + 1
    else:
        hi = mid

print(lo)

