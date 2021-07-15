# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 x = []
 y = []
 for i in range(4*n-1):
  a,b = list(map(int, input().split()))
  x.append(a)
  y.append(b)
 xs = set(x)
 ys = set(y)
 for i in xs:
  if x.count(i)%2!=0:
   p = i
   break
 for j in ys:
  if y.count(j)%2!=0:
   q = j
   break
 print(p,q)

