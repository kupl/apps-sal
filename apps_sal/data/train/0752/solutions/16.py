
d={}
n,q = list(map(int,input().split()))
for _ in range(n):
 a,b=input().strip().split()
 d[a]=b
for _ in range(q):
 f=input().strip()
 if "." in f:
  print(d.get(f.split(".")[-1],"unknown"))
 else:
  print("unknown")

