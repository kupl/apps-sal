import collections
from collections import defaultdict
import math




#for _ in range(1):
for _ in range(int(input())):
 #n=int(input())
 
 #k=int(input())
 p1,p2,k=[int(x) for x in input().split()]
 
 #c=[int(x) for x in input().split()]
 r = math.floor((p1+p2)/k)
 #rem=(p1+p2)%k    
 if r%2==0:
   print("CHEF")
 else:
  print("COOK") 



