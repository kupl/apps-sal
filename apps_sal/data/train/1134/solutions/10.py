#This is basic python file
#print "Hello Vedhika Fan!!!"
#print ""


import math # This will import math module

t = int(input())
while(t!=0):
 t-=1
 n,m = list(map(int,input().split()))
 num = list(map(int,input().split()))
#   energy = sum(num(0:m))
 energy = 0
 for i in range(m):
  energy+=num[i]
 for i in range(m,n):
  num[i] = math.ceil((num[i]+0.0)/2)
 flag = 1
 index = m
 while(index<n):
  energy-=(num[index])
  if(energy<0):
   flag = 0
   break
  index+=1
 if(flag == 0):
  print('DEFEAT')
 else:
  print('VICTORY')



