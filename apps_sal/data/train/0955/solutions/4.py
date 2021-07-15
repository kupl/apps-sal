import math
maxn = 10**4 + 1
x = [a for a in range(2,maxn)]
for y in x:
 for j in range(2,math.ceil(maxn/y)):
  if y*j in x:
   x.remove(y*j)
val = [0]*(3*(10**4))
for i in range(len(x)):
 for j in range(len(x)):
  val[(x[i]+2*x[j])]+=1
t=int(input())
for i in range(t):
 n=int(input())
 print(val[n])
