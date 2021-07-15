import math
for _ in range(int(input())):
 tt=int(input())
 x=y=moves=0
 while x<tt and y<(tt**2):
  x=math.floor(math.sqrt(y))+1
  y=y+x**2
  moves+=1 
 print(moves)
