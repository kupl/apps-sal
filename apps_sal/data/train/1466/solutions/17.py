n,q=map(int,input().split())
a=list(map(int,input().split()))
xor=0
sl=[]
for i in a:

 xor=xor^i
 sl.append(xor)
for i in range(q):
 qval=int(input())
 if(qval%(n+1)==0):
  print(0)
 else:
  print(sl[qval%(n+1)-1])
