import sys
t=int(input())
for _ in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    d={}
    for i in a:
        d[i]=d.get(i,0) + 1
    b=sorted(list(((list(d.values())))))
    ans=b[-1]
    ans1=b[-1]
    # print(b)
    # print(ans,ans1)
    for i in range(len(b)-2,-1,-1):
        # print(" ",b[i])
        # print("ans",ans,ans1,b[i])
        ans1=min(ans1-1,b[i])
        if ans1>0:
            ans+=ans1
        else:
            break
    print(ans)        
            
    

