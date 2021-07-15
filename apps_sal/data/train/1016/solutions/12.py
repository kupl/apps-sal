t=int(input())
while(t!=0):
 a = int(input())
 count = 0
 for i in range(a):
  c,b = list(map(int,input().split()))
  d = b-c
  if(d>5):
   count+=1
 print(count)
 t=t-1

