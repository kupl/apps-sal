n=int(input())
xy=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    if x>y:x,y=y,x
    xy.append((x,y))
xy.sort()
mn=10**12;mx=0
for i in range(n):
    x,y=xy[i]
    mn=min(mn,x)
    mx=max(mx,y)
cntmx=0;cntmn=0
for i in range(n):
    x,y=xy[i]
    if mx==y:cntmx+=1
    if mn==x:cntmn+=1
if cntmx==1 and cntmn==1 and xy[0][0]==mn and xy[0][1]==mx:
    rmn=xy[0][1];rmx=xy[0][1];bmn=xy[0][0];bmx=xy[0][0]
    for i in range(1,n):
        x,y=xy[i]
        rmn=min(rmn,y)
        rmx=max(rmx,y)
        bmn=min(bmn,x)
        bmx=max(bmx,x)
    print((rmx-rmn)*(bmx-bmn))
    return
else:
    rmn=10**12;rmx=0;bmn=10**12;bmx=0
    for i in range(n):
        x,y=xy[i]
        rmn=min(rmn,y)
        rmx=max(rmx,y)
        bmn=min(bmn,x)
        bmx=max(bmx,x)
ans1=(rmx-rmn)*(bmx-bmn)
xy.sort()
ymn=[10**12]*n
rmn=bmn;bmn=xy[0][0];bmx=xy[n-1][0]
for i in range(n):
    x,y=xy[i]
    ymn[i]=min(ymn[max(0,i-1)],y)
ans2=(rmx-rmn)*(bmx-bmn)
for i in range(n-1):
    x,y=xy[i]
    if ymn[i]<x:
        bmn=max(bmn,ymn[i-1])
        break
    bmn=x
    bmx=max(bmx,xy[max(0,i-1)][1])
    ans2=min(ans2,(rmx-rmn)*(bmx-bmn))
ans2=min(ans2,(rmx-rmn)*(bmx-bmn))
print(min(ans1,ans2))

