def sumsegtree(l,seg,st,en,x):
    if st==en:
        seg[x]=l[st]
    else:
        mid=(st+en)>>1
        sumsegtree(l,seg,st,mid,2*x)
        sumsegtree(l,seg,mid+1,en,2*x+1)
        seg[x]=seg[2*x]+seg[2*x+1]
 
def query(seg,st,en,val,x):
    if st==en:
        return seg[x]
    mid=(st+en)>>1
    if seg[2*x]>=val:
        return query(seg,st,mid,val,2*x)
    return query(seg,mid+1,en,val-seg[2*x],2*x+1)
 
def upd(seg,st,en,ind,val,x):
    if st==en:
        seg[x]=val
        return
    mid=(st+en)>>1
    if mid>=ind:
        upd(seg,st,mid,ind,val,2*x)
    else:
        upd(seg,mid+1,en,ind,val,2*x+1)
    seg[x]=seg[2*x]+seg[2*x+1]
 
n=int(input())
l=list(map(int,range(1,n+1)))
s=[0]*n
p=list(map(int,input().split()))
 
 
seg=["#"]*(n<<2)
sumsegtree(l,seg,0,len(l)-1,1)
 
for i in range(len(p)-1,-1,-1):
    s[i]=query(seg,1,n,p[i]+1,1)
    upd(seg,1,n,s[i],0,1)
 
print (*s)
