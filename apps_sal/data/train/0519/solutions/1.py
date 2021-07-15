a,b,*c=list(map(int,input().strip().split()))
d=[]
e=[]
for i in range(a):
    e.append(c[i])
    d.append(c[i+a])
DP1=[[-1 for i in range(a)] for j in range(a)]
def DP(l,r):
    nonlocal d,e,b,DP1
    if l>=r:
        return 0
    elif DP1[l][r]!=-1:
        return DP1[l][r]
    else:
        DP1[l][r]=max(DP1[l][r],DP(l+1,r))
        DP1[l][r]=max(DP1[l][r],DP(l,r-1))
        if d[l]+b==d[r]:
            DP1[l][r]=max(DP1[l][r],e[l]+e[r]+DP(l+1,r-1))
        for i in range(l,r):
            if d[l]+b==d[i] or d[i]+b==d[r]:
                DP1[l][r]=max(DP1[l][r],DP(l,i)+DP(i+1,r))
    return DP1[l][r]
print(DP(0,a-1))

