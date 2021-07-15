t=int(input())
for i in range(t):
 n=input()
 k=input()
 k=int(k)
 n=int(n)
 w=k%n
 if w==n/2:
  print(n-1)
 else:
  y=n-w
  y=min(y,w)
  print(2*y)

