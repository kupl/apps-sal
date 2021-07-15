t=int(input())
op=""
for j in range(0,t):
 n=int(input())
 d=dict()
 for i in range(0,n):
  s=input()
  tp=int(input())
  d[tp]=s
 for k in sorted(d):
  print(d[k])
print(op)
