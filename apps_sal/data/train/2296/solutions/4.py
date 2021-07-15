S=list(input())
N=len(S)
ord_A=ord("a")
alp=[0]*26
odd=-1
for i in range(N):
  m=ord(S[i])-ord_A
  alp[m]+=1
for k in range(26):
  if alp[k]%2==1:
    if odd==-1:
      odd=k
    else:
      print(-1)
      return
pos=[[] for i in range(26)]
Sequence=[0]*N
d=0
alp_num=[0]*26
for i in range(N):
  m=ord(S[i])-ord_A
  alp_num[m]+=1
  if 2*alp_num[m]<=alp[m]:
    Sequence[i]=d
    pos[m].append(d)
    d+=1
  elif m==odd and alp_num[m]==alp[m]//2+1:
    Sequence[i]=N//2
  else:
    j=pos[m].pop()
    Sequence[i]=N-1-j

def add(B,a,n):
    x = a
    while x<=n:
        B[x]+=1
        x+=x&(-x)
        
def sums(B,a):
    x=a
    S=0
    while x!=0:
        S+=B[x]
        x-=x&(-x)
    return S
  
def invnumber(n,A):
  B=[0]*(n*2+1)
  invs=0
  for i in range(n):
      s=A[i]+n
      invs+=sums(B,s)
      add(B,s,n*2)
  return n*(n-1)//2-invs

print(invnumber(N,Sequence))
