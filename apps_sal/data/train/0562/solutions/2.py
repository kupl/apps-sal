n,m=map(int,input().split())
chess=[]
for _ in range(n):
    chess.append([int(x) for x in list(input())])
chessO=[]
chessL=[]
fixO=[]
fixL=[]
for _ in range(n):
    p=[0]*m
    fixL.append(p)
    q=[0]*m
    fixO.append(q)
    tm=[0]*m
    chessO.append(tm)
    to=[0]*m
    chessL.append(to)

for i in range(n):
    for j in range(m):
        chessO[i][j]=((i+j)%2)^chess[i][j]
        chessL[i][j]=((i+j+1)%2)^chess[i][j]
        fixO[i][j]=chessO[i][j]
        fixL[i][j]=chessL[i][j]

for i in range(n):
    for j in range(1,m):
        fixO[i][j]=fixO[i][j-1]+chessO[i][j]
        fixL[i][j]=fixL[i][j-1]+chessL[i][j]

ans=[-1]*min(m,n)
for i in range(n):
    for j in range(m):
        for k in range(min(n-i,m-j)):
            errorO,errorL=0,0
            for l in range(i,i+k+1):
                errorO+=fixO[l][j+k]-fixO[l][j]+chessO[l][j]
                errorL+=fixL[l][j+k]-fixL[l][j]+chessL[l][j]
            if ans[k]==-1 or ans[k]>min(errorO,errorL): ans[k]=min(errorO,errorL)
final=[0]*50000
maxo=9999999999
for i in range(min(m,n)-1,-1,-1):
    if ans[i]!=-1 and ans[i]<maxo:
        maxo=ans[i]
        final[maxo]=i
tmp=final[0]
for i in range(1,50000):
    if  final[i]>tmp:
        tmp=final[i]
    final[i]=tmp
input()
q=[int(x) for x in input().split()]

for x in q:
    if x>50000-2 : print(final[45000]+1)
    else: print(final[x]+1)
    

