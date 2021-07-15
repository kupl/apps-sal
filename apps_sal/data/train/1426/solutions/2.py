# cook your dish here
for _ in range(int(input())):
 n,m=list(map(int, input().split()))
 c=list(map(int, input().split()))
 l=[0]*n 
 total=0
 
 for i in range(n):
  d,f,b=list(map(int, input().split()))
  if c[d-1]>0:
   c[d-1]-=1 
   total+=f 
   l[i]=d 
   
  else:
   total+=b 

 t=m-1 
 print(total) 
 for i in l:
  if i>0:
   print(i, end=' ')
   
  else:
   while True:
    if c[t]>0:
     print(t+1, end=' ')
     c[t]-=1
     if c[t]==0:
      t-=1 
     break
    
    else:
     t-=1 
   
 print('') 
