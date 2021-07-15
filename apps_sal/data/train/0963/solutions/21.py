def large(a,i,j):
    b=i
    maxo=a[i]
    t=i
    while(b<=j):
        if(a[b]>maxo):
            maxo=a[b]
            t=b
        b=b+1
    
    return t
def f(a,i,j,count):
    p=large(a,i,j)
    if(p==i or p==j):
        count=count+1
        return count
    else:
        return min(f(a,i,p-1,count+1),f(a,p+1,j,count+1))
t=int(input())
for x in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(f(a,0,n-1,0))

