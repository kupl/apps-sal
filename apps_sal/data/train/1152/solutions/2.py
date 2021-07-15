# cook your dish here
n=int(input())
d=dict()
for _ in range(n):
 aa=input().split()
 s=aa[0]
 v=int(aa[1])
 d[s]=v
q=int(input())
for _ in range(q):
 qi=input()
 value=None
 recep=None
 for i in d:
  if i.startswith(qi):
   if value is None or value<d[i]:
    value=d[i]
    recep=i
 if recep==None:
  print("NO")
 else:
  print(recep)
