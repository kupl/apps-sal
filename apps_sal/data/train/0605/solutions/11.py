t=int(input())
for l in range(t):
 n,m=list(map(int,input().split()))
 a=False
 s=input()
 for i in range(1,n+1):
  
  for j in range(1,m+1):
   x=i
   y=j
   loulou=False
   for h in range(len(s)):
    
    if s[h]=='L':
     y=y-1
    elif s[h]=='R':
     y=y+1
    elif s[h]=='U':
     x=x+1
    else:
     x=x-1
    if x<1 or x>n or y<1 or y>m :
     loulou=True
     
     break
     
    
    
   if loulou==False :
    a=True
    
    print('safe')
    break
  if a==True:
   break
 if a==False:
  print('unsafe')

