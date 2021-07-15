from pprint import pprint
from numpy import where
arr =[]
from sys import stdin,stdout
for _ in range(int(stdin.readline())):
 t = int(stdin.readline())
 a = []
 for i in range(4):
  temp = []
  for j in range(4):
   temp.append(0)
  a.append(temp)
 s = 0
 for __ in range(t):
  mov , time = input().split()
  time = int(time)
  if mov == 'A':
   if time == 12:
    a[0][0]+=1
   elif time ==3:
    a[0][1]+=1
   elif time == 6:
    a[0][2]+=1
   else:
    a[0][3]+=1
  elif mov =='B':
   if time == 12:
    a[1][0]+=1
   elif time == 3:
    a[1][1]+=1
   elif time == 6:
    a[1][2]+=1
   else:
    a[1][3]+=1
  elif mov =='C':
   if time == 12:
    a[2][0]+=1
   elif time == 3:
    a[2][1]+=1
   elif time == 6:
    a[2][2]+=1
   else:
    a[2][3]+=1
  else:
   if time == 12:
    a[3][0]+=1
   elif time == 3:
    a[3][1]+=1
   elif time == 6:
    a[3][2]+=1
   else:
    a[3][3]+=1
 ma = -1
 cakes =[]
 for k in range(4):
  mai,maj=-1,-1
  for i in range(4):
   for j in range(4):
    if a[i][j] > ma:
     ma = a[i][j]
     mai = i
     maj = j
  for z in range(4):
   for x in range(4):
    if z==mai or x == maj:
     a[z][x]=0
  cakes.append(ma)
  ma = -1
 for i in range(len(cakes)):
  if cakes[i]==0:
   s-=100
  else:
   if i==0:
    s+= cakes[i]*100
   elif i==1:
    s+= cakes[i]*75
   elif i==2:
    s+= cakes[i]*50
   elif i==3:
    s+= cakes[i]*25
 print(s)
 arr.append(s)
 #print(arr)
print(sum(arr))
