import sys

num=int(sys.stdin.readline())
s=sys.stdin.readline().split()
sky=list(map(int,s))
sky.reverse()
cuts=0
change=0
t=False
i=1

while i<len(sky):
 if sky[i]<=sky[i-1]:
  for j in range(i-1,-1,-1):
   
   if sky[j]<=sky[i]-(i-j):
    break
   else:
    change+=sky[j]-(sky[i]-(i-j))
    
   if change>=sky[i]:
    change=sky[i]
    t=True
    break
    
  cuts+=change
  
  if t:
   del sky[i]
   t=False
   i-=1
   
  else:
   for j in range(i-1,-1,-1):
    if sky[j]<sky[i]-(i-j):
     break
    else:
     sky[j]=sky[i]-(i-j)
 i+=1
    
 change=0
     
print(cuts)

