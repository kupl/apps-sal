import math
for _ in range(int(input())):
 A,B = map(int,input().split(" "))
 c = 0
 d = 0
 sum = 0
 sum1 = 0
 for n in range(1,A+1,2):
  sum+=n
  if(sum<=A):
   c+=1
 for m in range(2,B+1,2):
  sum1+=m
  if(sum1<=B):
   d+=1
 #print(c,d)
 if(c>d):
  print("Limak")
 else:
  print("Bob")
