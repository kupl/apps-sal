#

#for _ in range(int(input())):
n,m,x = list(map(int,input().split()))
arr = [[0 for i in range(m)] for j in range(n)]
dpr = [0]*n 
dpc = [0]*m
for i in range(x):
    a,b=list(map(int,input().split()))
    arr[a][b]=1
    dpr[a]+=1 
    dpc[b]+=1
#print(dpr,dpc)
max=-1
for i in range(n):
    for j in range(m):
        sum=dpr[i]+dpc[j]
        #print(i,j,sum)
        if arr[i][j]==1:
            sum-=1
        if sum>max:
            max=sum
print(max)

        

