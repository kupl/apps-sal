# cook your dish here
n,m=map(int,input().split())
L=[]
for i in range(n):
    s=input()
    L.append(s)

cost=[]
h2=[0]*(m+1)
cost.append(h2)
for i in range(n):
    h=[0]
    for j in range(m):
        if(L[i][j]=='0' and (i+j)%2!=0):
            h.append(1)
        elif(L[i][j]=='1' and (i+j)%2==0):
            h.append(1)
        else:
            h.append(0)
    cost.append(h)

pre=[]
h2=[0]*(m+1)
pre.append(h2)
for i in range(1,n+1):
    h=[0]
    c=0
    for j in range(1,m+1):
        c+=cost[i][j]
        c2=c
        if(i>0):
            c2+=pre[i-1][j]
        h.append(c2)
    pre.append(h)

bs=[0]*((m*n)+10)

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,min(m,n)+1):
            if(i-k>=0 and j-k>=0):
                c=pre[i][j]-pre[i-k][j]-pre[i][j-k]+pre[i-k][j-k]
                c=min(c,(k*k)-c)
                bs[c]=max(bs[c],k)

mx=bs[0]
for i in range(1,len(bs)):
    mx=max(mx,bs[i])
    bs[i]=mx

Q=int(input())
q=[int(x) for x in input().split()]
for i in range(0,len(q)):
    qr=min(m*n,q[i])
    print(bs[qr])



