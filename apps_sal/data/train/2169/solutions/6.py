from sys import stdin
n,p,k=list(map(int,stdin.readline().strip().split()))
s=list(map(int,stdin.readline().strip().split()))
st=set()
d=dict()
for i in s:
    x=(i**4-i*k)%p
    if x in st:
        d[x]+=1
    else:
        st.add(x)
        d[x]=1
s.sort()
ans=0
for i in s:
    x=(i**4-i*k)%p
    if x in st:
        ans+=(d[x]-1)*d[x]//2
        d[x]=0
print(ans)
    

