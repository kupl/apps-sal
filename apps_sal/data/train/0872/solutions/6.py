import math
for i in range(int(input())):
 n,a,b,k=list(map(int,input().split()))
 lcm=(a*b)/math.gcd(a,b)
 #print(lcm)
 z=(n//a) + (n//b)-2*(n//lcm)
 #print(z)
 if z>=k:
  print("Win")
 else:
  print("Lose")

