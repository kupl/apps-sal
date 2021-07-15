f=input
from bisect import bisect_left as g, insort as h
n,s=int(f()),list(f())
d={chr(97+i):[] for i in range(26)}
for i in range(n): d[s[i]]+=[i]
for _ in range(int(f())):
  a,b,c=f().split(); b=int(b)-1
  if a>'1': print(sum(1 for l in d.values() if g(l,b)<len(l) and l[g(l,b)]<int(c)))
  elif s[b]!=c: l=d[s[b]]; l.pop(g(l,b)); s[b]=c; h(d[c],b)
