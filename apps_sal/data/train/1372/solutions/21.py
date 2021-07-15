import math
for _ in range(int(input())):
 x1,y1,x2,y2 = map(int,input().split())
 dis1 = math.sqrt(pow(x1-0,2) + pow(y1-0,2))
 dis2 = math.sqrt(pow(x2-0,2) + pow(y2-0,2))
 if dis1 > dis2:
  print('B IS CLOSER')
 else:
  print('A IS CLOSER')
