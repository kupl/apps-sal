from collections import defaultdict
import bisect
t = int(input())
for i in range(t):
    n = int(input())
    A = [int(j) for j in input().split()]
    d = defaultdict(list)
    for j,i in enumerate(A):
        d[i].append(j)
    #print(d)
    keys = sorted(d.keys())
    #print(keys)
    pk = 0
    ans = 1
    prev = None
    for i in keys:
        pos = bisect.bisect_left(d[i],pk)
        if pos==len(d[i]):
            pos = 0
            ans+=1
        pos = d[i][pos]
        pk = pos
        #print(pk)
    print(ans)
        
        

