D=[0]*31
D[1]=2
D[2]=5

for i in range(3,31):
 best=10**10
 for p in range(1,i+1):
  best=min(best,D[p-1]+D[i-p]+i+1)
 D[i]=best

t=int(input())
for i in range(t):
 n,m=list(map(int,input().split()))
 maxi=(n+2)*(n+1)/2-1
 mini=D[n]
 if mini<=m<=maxi: print(0)
 elif m<mini: print(-1)
 else: print(m-maxi)

