# -*- coding: utf-8 -*-
"""
@author: coding_don
"""
import sys
#sys.stdin = open('ip.txt', 'r') 
#sys.stdout = open('op.txt', 'w')
try:
 
 def main():
  t=1
  # t=int(sys.stdin.readline())
  while(t):
   n,m=[int(x) for x in sys.stdin.readline().split()]
   a=[]
   update=[]
   for i in range(n):
    tmp=sys.stdin.readline()
    a.append(tmp)
    update.append([0 for j in range(m+1)])
   update.append([0 for j in range(m+1)])
   q=int(sys.stdin.readline())
   while(q):
    x1,y1,x2,y2=[int(z) for z in sys.stdin.readline().split()]
    update[x1][y1]+=1
    if(x2<n):
     update[x2+1][y1]+=-1
    if(y2<m):
     update[x1][y2+1]+=-1
    if(x2<n and y2<m):
     update[x2+1][y2+1]+=1
   
    q-=1

   for i in range(1,n+1):
    for j in range(1,m+1):
     update[i][j]+=update[i][j-1]

   for j in range(1,m+1):
    for i in range(1,n+1):
     update[i][j]+=update[i-1][j]
   for i in range(1,n+1):
    for j in range(1,m+1):
     if(update[i][j]%2==0):
      sys.stdout.write(a[i-1][j-1])
     else:
      sys.stdout.write(str(1-(ord(a[i-1][j-1])-48)))

    sys.stdout.write('\n')

   t-=1
  
 main()
  
except Exception as e:
 sys.stdout.write("ErrOR : "+str(e))
