t=int(input())
def fun(n,a):
    ans=[]
    for i in range(2*n):
        if ans.count(a[i])==0:
            ans.append(a[i])
    print(*ans,sep=" ")
while t:
    t-=1
    n=int(input())
    a=[int(i) for i in input().split()]
    fun(n,a)

