t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=a[0:k]
    a.extend(b)
    i=0
    s=sum(a[i:i+k])
    i=k
    temp=s
    while(i<n+k-1):
        temp=temp+a[i]-a[i-k]
        if(temp>s):
            s=temp
        i+=1
    print(s)
