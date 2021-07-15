q=int(input())
for i in range(q):
    a,b=list(map(int,input().split()))
    left=0
    right=a*b
    for i in range(100):
        mid=(left+right)//2
        if mid*mid<a*b:
            left=mid
        else:
            right=mid
    ret=left*2
    if ret==0:
        print(ret)
        continue
    if (a*b-1)//left==left:
        ret-=1
    if min(a,b)<=left:
        ret-=1
    print(ret)

