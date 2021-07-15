a=[0]*4
n,k=list(map(int,input().split()))
for i in range(4):
    a[i]=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    a[0].append(a[3][i])
    a[1].append(a[2][i])
ans=[]
def check():
    nonlocal k
    for i in range(2*n):
        if a[0][i]==a[1][i] and a[0][i]!=0:
            if i<n:
                ans.append([a[1][i],0,i])
            else:
                ans.append([a[1][i],3,2*n-i-1])
            k-=1
            a[0][i]=a[1][i]=0
def fuck():
    step=-1
    for i in range(2*n):
        if a[1][i]==0:
            step=i
            break
    if step==-1:
        return False
    else:
        for i in range(2*n-1):
            x=(step+i)%(2*n)
            y=(step+1+i)%(2*n)
            if a[1][y]!=0:
                a[1][x]=a[1][y]
                if x==n-1 and y==n:
                    ans.append([a[1][y],1,n-1])
                elif x==0 and y==0:
                    ans.append([a[1][y],2,0])
                elif x<n:
                    ans.append([a[1][y],1,x])
                else:
                    ans.append([a[1][y],2,2*n-x-1])
                a[1][y] = 0
        return True
check()
while k!=0:
    if fuck()==False:
        print(-1)
        return
    check()
print(len(ans))
for i in ans:
    x,y,z=i
    print(x,y+1,z+1)





