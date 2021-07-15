# cook your dish here
def find_gcd(x, y): 
 while(y): 
  x, y = y, x % y 
 
 return x 
n=int(input())
for i in range(n):
 n1=int(input())
 l=list(map(int,input().split()))
 if(n1==1):
  print(l[0],1)
 else:    
  num1=l[0] 
  num2=l[1] 
  gcd=find_gcd(num1,num2) 
  for i in range(2,len(l)): 
   gcd=find_gcd(gcd,l[i]) 
  sum1=0 
  for i in range(n1):
   sum1+=(l[i]//gcd)
  print(gcd,int(sum1)) 

