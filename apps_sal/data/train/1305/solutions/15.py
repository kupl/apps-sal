# cook your dish here
try:
 for i in range(int(input())):
  n=int(input())
  li=[]
  for j in range(n):
   li.append(list(map(int,input().split())))
  x=0
  for k in range(n):
   for j in range(n):
    if(k!=n-1 and j!=n-1):
     if(li[k][j]==1):
      if(li[k][j+1]==1 or li[k+1][j]==1):
       #print(k,' ',j,' ','1')
       x=1
       break
       
    elif(j==n-1 and k!=n-1):
     if(li[k][j]==1):
      if(li[k+1][j]==1):
       x=1
       #print(k,' ',j,' ','2')
       break
    elif(k==n-1 and j!=n-1):
     if(li[k][j]==1):
      if(li[k][j+1]==1):
       x=1
       #print(k,' ',j,' ','3')
       break
   if(x==1):
    print('UNSAFE')
    break
  if(x==0):
   print('SAFE')
   
except:
 pass

