# cook your dish here
import sys

N=int(sys.stdin.readline())
A=[int(i) for i in sys.stdin.readline().split()]

dp1=[]
dp2=[]

for i in range(N+1):
    dp1.append([-1,-1])
    dp2.append([-1,-1])

# dp1 initializations    
dp1[0][0]=0
dp1[0][1]=0
dp1[1][0]=0
dp1[1][1]=2e9

# dp2 initializations
dp2[0][0]=0
dp2[0][1]=0
dp2[1][0]=2e9
dp2[1][1]=A[0]

for x in range(2,N+1):
    dp1[x][0]=dp1[x-1][1]
    dp1[x][1]=min(dp1[x-1][0],dp1[x-1][1])+A[x-1]
    
    dp2[x][0]=dp2[x-1][1]
    dp2[x][1]=min(dp2[x-1][0],dp2[x-1][1])+A[x-1]

ans=min(min(dp1[N][1],dp2[N][0]),dp2[N][1])
print(ans)
    

