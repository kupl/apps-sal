t=int(input())
import sys
while(t!=0):
    n,m=list(map(int,input().strip().split()))
    a=list(map(int,input().strip().split()))
    l=[0]*100000
    mx=-1
    c=0
    for i in a:
        if(i>mx):
            mx=i
        l[i]+=1
    for i in range(1,mx+1):
        if(l[i]==0):
            if(i==m):
                print(n)
                c=1
                break
            elif(i<m):
                print(-1)
                c=1
                break
            else:
                print(n-l[m])
                c=1
                break
    if(c==0):
        if(m==mx+1):
            print(n)
        else:
            print("-1")
    t-=1
