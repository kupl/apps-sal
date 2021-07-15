import sys
import bisect as b
input=sys.stdin.readline
li=[]
mod=10**9 + 7
mxr=100
mxn=20000000

for _ in range(int(input())):
 l,r=map(int,input().split())
 li.append([l,r])
 mxr=max(mxr,r+1)

g=[0,1,2]
p=[0,1,3]
s=[0,1,9]

for i in range(3,mxn):
 gg=1+g[i-g[g[i-1]]]
 pp=(p[i-1]+gg)%mod
 ss=(s[i-1]+gg*i*i)%mod
 g.append(gg)
 p.append(pp)
 s.append(ss)
 if pp>mxr:
  break
def solve(m):
 n=b.bisect_right(p,m)
 return (s[n-1] + ((m-p[n-1])*n*n))%mod
for l,r in li:
 ans=(solve(r)-solve(l-1))%mod
 print(ans)
