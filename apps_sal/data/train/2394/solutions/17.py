t=int(input())
def fun(n,a):
    ans=0
    count=0
    i=0
    while i<n:
        if a[i]=="(":
            count+=1
        else:
            count-=1
        i+=1
        if count<0:
            ans+=1
            count+=1
    print(int(ans))
while t:
    t-=1
    n=int(input())
    a=input()
    fun(n,a)

