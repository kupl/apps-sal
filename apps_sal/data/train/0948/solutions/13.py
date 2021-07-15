a,b=str(input()).split(" ")
a=int(a)
b=int(b)
count=0
for i in range(1,a+1):
 for j in range(1,b+1):
  a1=i*i+j
  a2=a1**(0.5)
  a3=int(a2)
  if(a3==a2):
   count+=1
print(count) 
