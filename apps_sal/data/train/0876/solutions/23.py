n=int(input())
for i in range(1,n+1):
    r=[int(r)for r in input().split()]
    y=[int(y)for y in input().split()]
    y.sort()
    j=0
    j=r[0]
    diff=int(y[j-1]-y[0])
    if(diff < r[1]):
        print("YES")
        diff=0
    else:
        print("NO")
        diff=0

