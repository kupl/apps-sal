for _ in range(int(input())):
 N,M = map(int,input().split())
 a,b = M//4,M%4
 c,d = M//3,M%3 
 strdn1,strdn2,ans='1 1 2 2 ','1 2 3 ',''
 if N==1 and M==1:
  print(1,1,sep="\n")
 elif N==1:
  if M==2:
   print(1)
  else:
   print(2)
  for i in range(1,a+1):
   ans = ans + strdn1
  if b!=0:
   ans = ans+ strdn1[:2*b-1]
  print(ans)
 elif M==1:
  if N==2:
   print(1)
  else:
   print(2)
  for i in range(1,N+1):
   if i%4==1 or i%4==2:
    print(1)
   else:
    print(2)
 elif N==2 and M==2:
  print('2','1 1','2 2',sep="\n")
 elif N==2:
  print(3)
  for i in range(1,c+1):
   ans = ans + strdn2
  if d!=0:
   ans = ans+ strdn2[:2*d-1]
  print(ans)
  print(ans)
 elif M==2:
  print(3)
  for i in range(1,N+1):
   if i%3==0:
    print('3 3')
   else:
    print(str(i%3)+' '+str(i%3))
 else:
  print(4)
  str1,str2='1 2 3 4 ','3 4 1 2 '
  for i in range(1,N+1):
   ans=''
   if i%4==1 or i%4==2:
    for i in range(1,a+1):
     ans = ans + str1
    if b!=0:
     ans = ans+ str1[:2*b-1]
    print(ans)
   else:
    for i in range(1,a+1):
     ans = ans + str2
    if b!=0:
     ans = ans+ str2[:2*b-1]
    print(ans)
    
    
  
  
   
  
