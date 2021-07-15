import math
Mod=1000000007

for _ in range(int(input())):
  v=int(input())
  i=0
  s=0
  for i in range(1,math.floor(math.sqrt(v))+1):
    s+=i*((math.floor(v/i))*(math.floor(v/i)+1)-(i*(i-1)))
    s-=(i*i)
  print(s%Mod) 

