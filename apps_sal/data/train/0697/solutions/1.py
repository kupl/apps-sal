def call(lst,m):
    maxsum= sum(lst[0:m])
    j=0
    maxs=0
    for i in range(m,len(lst)):
        maxs = max(maxsum,maxs)
        #print(maxsum,lst[j],lst[i])
        maxsum -= lst[j]
        maxsum += lst[i]
        j = j+1
    maxs = max(maxsum,maxs)
    return maxs
t = int(input())
while(t):
    t = t-1
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    print(call(lst,m))
