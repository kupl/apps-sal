for _ in range(int(input())):
 n,m = map(int,input().split())
 pos = list(map(int,input().split()))
 a = max(pos)
 p = a
 x = []
 j = 0
 for i in range(n):
  if i!=a and i<a:
   x.append(p)
   p-=1
  else:
   x.append(j)
   j+=1
 b = min(pos)
 p = b
 y = []
 j = 0
 for i in range(n):
  if i!=b and i<b:
   y.append(p)
   p-=1
  else:
   y.append(j)
   j+=1
 for i in range(len(y)):
  if x[i]>y[i]:
   print(x[i],end = " ")
  else:
   print(y[i],end = " ")
 print()

