import math
for i in range(int(input())):
 z,a,b,k=list(map(int,input().split())) 
 n=0
 x1=z//a 
 x2=z//b 
 x3=(a*b)//math.gcd(a,b) 
 p1=x1-z//x3 
 p2=x2-z//x3 
 if p1+p2>=k:
  print('Win') 
 else:
  print('Lose') 
   

