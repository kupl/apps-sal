t=int(input())
for i in range(t):
 res=[]
 n,m=map(int,input().strip().split())
 p = set(map(int,input().strip().split()))
 l,r=min(p),max(p)
 nl = []
 for j in range(n):
  nl.append(str(max(abs(r-j),abs(j-l))))
 res.append(' '.join(nl))
 for h in range(len(res)):
  print(res[h])
