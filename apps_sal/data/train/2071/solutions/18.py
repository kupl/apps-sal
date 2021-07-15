def count(t):
  return sum(v*(v-1)//2 for v in t.values())
a,b,c={},{},{}
n=int(input())
for _ in range(n):
  x,y=map(int,input().split())
  a[x]=a.get(x,0)+1
  b[y]=b.get(y,0)+1
  c[(x,y)]=c.get((x,y),0)+1
print(count(a)+count(b)-count(c))
