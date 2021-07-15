# cook your dish here
t=int(input())
for _ in range(t):
 a=int(input(),2)
 b=int(input(),2)
 c=0
 while b>0:
  x=a^b 
  v=a&b 
  a=x 
  b=v*2 
  c+=1 
 print(c)
