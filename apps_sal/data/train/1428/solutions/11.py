# cook your dish here
import heapq
from math import ceil
for i in range(int(input())):
 n,a,b,x,y,z = list(map(int,input().split()))
 cntrbtns= [-(int(x)) for x in input().split()]
 
 if b>=z :
  print("RIP")
  continue
 t=ceil((z-b)/y)
 sum= a+ x*(t-1) 
 c=0
 heapq.heapify(cntrbtns)
 ele=0
 while True:
  if sum>=z:
   print(c)
   break
  ele=-ele
  ele=heapq.heappushpop(cntrbtns,-(ele>>1))
  if ele==0:
   print("RIP")
   break
  sum-=ele 
  c+=1 
  

