import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))
if k==0:
    print(0)
    return

A=sorted(map(int,input().split()))

# DP[UL][n][left]
# [left*pow(2,n),left*pow(2,n)+pow(2,n))の間のチームで,
# ファンのチームが
# UL=0: upperでもlowerでも勝ち残っている
# UL=1: upperでのみ勝ち残っている
# UL=2: lowerでのみ勝ち残っている
# ときの、そこまでのファンのチームの試合数の最大値.

DP=[[[0]*((1<<n)+2) for i in range(n+1)] for UL in range(3)]

for i in range(k):
    if A[i]%2==1:
        DP[1][1][A[i]]=1
        DP[2][1][A[i]]=1
    else:
        DP[1][1][A[i]-1]=1
        DP[2][1][A[i]-1]=1

    if i<k-1 and A[i]%2==1 and A[i+1]==A[i]+1:
        DP[0][1][A[i]]=1
        
for i in range(2,n+1):
    for left in range(1,(1<<n)+1,1<<i):

        if DP[0][i-1][left]:
            DP[0][i][left]=max(DP[0][i-1][left] + DP[0][i-1][left+(1<<(i-1))] + 3,DP[0][i-1][left] + DP[1][i-1][left+(1<<(i-1))] + 3,\
                               DP[0][i-1][left] + DP[2][i-1][left+(1<<(i-1))] + 3)
            
        if DP[0][i-1][left+(1<<(i-1))]:
            DP[0][i][left]=max(DP[0][i][left], DP[0][i-1][left] + DP[0][i-1][left+(1<<(i-1))] + 3,\
                               DP[1][i-1][left] + DP[0][i-1][left+(1<<(i-1))] + 3,DP[2][i-1][left] + DP[0][i-1][left+(1<<(i-1))] + 3)

        if DP[1][i-1][left]:
            DP[1][i][left]=max(DP[1][i][left], DP[1][i-1][left] + 1)
            DP[2][i][left]=max(DP[2][i][left], DP[1][i-1][left] + 2)

        if DP[2][i-1][left]:
            DP[2][i][left]=max(DP[2][i][left], DP[2][i-1][left] + 2)

        if DP[1][i-1][left+(1<<(i-1))]:
            DP[1][i][left]=max(DP[1][i][left], DP[1][i-1][left+(1<<(i-1))] + 1)
            DP[2][i][left]=max(DP[2][i][left], DP[1][i-1][left+(1<<(i-1))] + 2)

        if DP[2][i-1][left+(1<<(i-1))]:
            DP[2][i][left]=max(DP[2][i][left], DP[2][i-1][left+(1<<(i-1))] + 2)


        if DP[1][i-1][left] and DP[1][i-1][left+(1<<(i-1))]:
            DP[0][i][left]=max(DP[0][i][left], DP[1][i-1][left] + DP[1][i-1][left+(1<<(i-1))] + 2)

        if DP[1][i-1][left] and DP[2][i-1][left+(1<<(i-1))]:
            DP[0][i][left]=max(DP[0][i][left], DP[1][i-1][left] + DP[2][i-1][left+(1<<(i-1))] + 3)

        if DP[2][i-1][left] and DP[1][i-1][left+(1<<(i-1))]:
            DP[0][i][left]=max(DP[0][i][left], DP[2][i-1][left] + DP[1][i-1][left+(1<<(i-1))] + 3)

        if DP[2][i-1][left] and DP[2][i-1][left+(1<<(i-1))]:
            DP[2][i][left]=max(DP[2][i][left], DP[2][i-1][left] + DP[2][i-1][left+(1<<(i-1))] + 2)


"""                          
for i in range(n+1):
    print(DP[0][i])
print()
for i in range(n+1):
    print(DP[1][i])
print()
for i in range(n+1):
    print(DP[2][i])
print()
for i in range(n+1):
    print(DP[0][0][i])
"""
print(max(DP[0][n][1],DP[1][n][1],DP[2][n][1])+1)

