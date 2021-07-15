t=int(input())
for w in range(t):
 inp = list(map(int,input().split()))
 row=inp[0]
 col=inp[1]
 flag=0
 if(min(row,col)==1):
  if(max(row,col)>=3):
   print(2)
  else:
   print(1)
  if(1):
   a=[0 for i in range(max(col,row))]
   count=0
   it=1
   for i in range(max(col,row)):
    if(count==2):
     if(it==1):
      it=2
     else:
      it=1
     a[i]=it
     count=1
     continue
    else:
     a[i]=it
     count+=1
   if(row==1):
    for item in a:
     print(item,end=" ")
    print(" ")
   
   else:
    for item in a:
     print(item)
 elif(min(row,col)==2):
  if(max(row,col)==2):
   print(2)
   print(2,end=" ")
   print(2)
   print(1,end=" ")
   print(1)
  else:
   a=[[0 for i in range(max(row,col))]for j in range(2)]
   print(3)
   it=3
   count=1
   for i in range(max(row,col)):
    if(count==1):
     a[0][i]=it
     count+=1
     continue
    else:
     if(count==2):
      it-=1
      if(it==0):
       it=3
      a[0][i]=it
      count=1
      continue
   it=2
   count=2
   for i in range(max(row,col)):
    if(count==1):
     a[1][i]=it
     count+=1
     continue
    else:
     if(count==2):
      it-=1
      if(it==0):
       it=3
      a[1][i]=it
      count=1
      continue
   if(row==2):
    for i in range(max(row,col)):
     print(a[0][i],end=" ")
    print(" ")
    for i in range(max(row,col)):
     print(a[1][i],end=" ")
    print(' ')
   else:
    for i in range(max(row,col)):
     print(a[0][i],end=" ")
     print(a[1][i])

 else:
  print(4)
  a=[[0 for i in range(col)]for j in range(row)]
  a[0][0]=2
  a[1][0]=2
  a[0][1]=3
  a[1][1]=3
  for i in range(2,col,2):
   if(a[0][i-2]==2):
    a[0][i]=1
    a[1][i]=1
   else:
    a[0][i]=2
    a[1][i]=2
  for i in range(3,col,2):
   if(a[0][i-2]==3):
    a[0][i]=4
    a[1][i]=4
   else:
    a[0][i]=3
    a[1][i]=3
  for i in range(col):
   for j in range(2,row):
    if(a[j-2][i]==2):
     a[j][i]=1
    elif(a[j-2][i]==1):
     a[j][i]=2
    elif(a[j-2][i]==3):
     a[j][i]=4
    elif(a[j-2][i]==4):
     a[j][i]=3
  for i in range(row):
   for j in range(col):
    print(a[i][j],end=' ')
   print(" ")
