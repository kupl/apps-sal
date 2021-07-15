N=int(input())
d=0
s=10**9+1
for i in range(N):
  a,b=map(int, input().split())
  d+=a
  if a>b:
    s=min(s,b)
if s==10**9+1:
  print(0)
  return
print(d-s)
