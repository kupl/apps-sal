a,b=map(int,input().split())
c=0
for i in range(1,a+1):
 for j in range(1,b+1):
  a1=i*i+j
  a2=a1**(0.5)
  a3=int(a2)
  if(a3==a2):
   c+=1
print(c) 
