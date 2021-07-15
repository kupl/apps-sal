n=int(input())
for i in range(n):
    ans=0
    t,k=map(int,input().split())
    ans+=(k+2)*(t//2)
    if t%2==1:
        ans+=1+2*k
    print(ans)
