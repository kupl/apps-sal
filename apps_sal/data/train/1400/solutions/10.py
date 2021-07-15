for u in range(int(input())):
 n,x,y=list(map(int,input().split()))
 a,b=0,0
 a=(n-x)
 for i in range(x):
  a+=2**i
 for i in range(y):
  b+=2**i
 b+=((n-y)*(2**(y-1)))
 print(a,b)

