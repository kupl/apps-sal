n=int(input())
for _ in range(n):
    n1=int(input())
    ans=0
    l=input().split()
    for i in l:
        if int(i)%6==0:
            ans+=6
        else:
            ans+=int(i)%6
    print(ans)

