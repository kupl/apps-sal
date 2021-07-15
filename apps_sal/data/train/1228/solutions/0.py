for _ in range(int(input())):
 n=int(input())
 a=[]
 b=[]
 for i in range(4*n-1):
  c,d=list(map(int,input().split()))
  a.append(c)
  b.append(d)
 c1=0
 c2=0
 for i in a:
  c1^=i
 for i in b:
  c2^=i
 print(c1,c2)
