# cook your dish here
try:
 t=int(input())
 for i in range(t):
  rc=int(input())
  matr=[]
  flag=0
  for i in range(rc):
   matr.append(list(map(int,input().split())))
 #    print(matr)
  for i in range(rc-1):
   for j in range(rc-1):
    if(matr[i][j]==1):
     if(matr[i+1][j]==1 or matr[i][j+1]==1):
      flag=1
      break
    if(flag==1):
     break
  if(flag==1):
   print("UNSAFE")
  else:
   print("SAFE")
except:
 pass

