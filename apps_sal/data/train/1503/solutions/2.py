# cook your dish here
import math 
for _ in range(int(input())):
 x,y=list(map(int,input().split()))
 print(x//math.gcd(x,y)*y//math.gcd(x,y))
 
 


