def show(t):
 for _ in range(t):
  a,n = map(int,input().rstrip().split())
  res = []
  res1 = []
  a = str(a)
  for i in a:
   res.append(int(i))
  a = n
  for i in range(len(res)-1,-1,-1):
   if a>=res[i]:
    a = res[i]
    res1.append(a)
  for i in range(len(res1)-1,-1,-1):
   print(res1[i],end="")
  for i in range(len(res)-len(res1)):
   print(n,end="")
  print("")
show(int(input()))
