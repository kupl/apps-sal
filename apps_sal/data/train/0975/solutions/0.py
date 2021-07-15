for _ in range(int(input())):
 n,r,x,y=map(int,input().split())
 if x>0:
  a=list(map(int,input().split()))
 if y>0:
  b=list(map(int,input().split()))
 if x>0 and y>0:
  a=a+b
  c=n-len(list(set(a)))
 else:
  l=x+y
  c=n-l
 x=min(c,r)
 print(x)
