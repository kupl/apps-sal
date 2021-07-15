ans = []
n = int(input())
arr = list(map(int,input().split()))
for x in arr:
    lo,hi = 0,len(ans)
    while(lo < hi):
        mid = (lo+hi)//2
        if(ans[mid][-1] < x):
            hi = mid
        else:
            lo = mid+1
    if(lo == len(ans)):
        ans.append([x])
    else:
        ans[lo].append(x)
for line in ans:
    print(' '.join([str(i) for i in line]))

