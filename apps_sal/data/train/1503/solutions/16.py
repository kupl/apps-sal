# cook your dish here
a= int(input())
for i in range(a):
 rect= input()
 rect= rect.split(" ")
 b= int(rect[0])
 l= int(rect[1])
 # print(b,l)
 maxx=1
 
 for i in range(1,b+1):
  if(b%i==0 and l%i==0):
   maxx=i

 print(l//maxx * b//maxx)
  
 

