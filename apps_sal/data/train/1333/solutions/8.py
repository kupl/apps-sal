m = pow(10,9)+7
t = int(input())
while t>0:
 n = int(input())
 a = list(map(int,input().split()))
 c = 1
 f = a[0]
 for i in range(1,n):
  # p = bin(f)[2:]
  # q = bin(a[i])[2:]
  p = f
  q = a[i]
  g = p&q
  if g != p:
   c = 0
   break
  # print(pow(2,bin(f)[2:].count("1")))
  f = a[i]
  c = c*pow(2,bin(g)[2:].count("1"))%m
  # print(c)
 print(c)
 t = t-1
