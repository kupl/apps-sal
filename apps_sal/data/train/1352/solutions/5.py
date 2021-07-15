t = int(input())
r=0
while t:
 t-=1
 n = int(input())
 a = input().split()
 a = [int(i) for i in a]
 x=max(a)
 for i in range(x+1):
  cnt = a.count(i)
  if cnt:
   print(str(i)+":",cnt)
   
 

