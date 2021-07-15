from decimal import *
for i in range(int(input())):
 x, y = input().split()
 x = int(x)
 y = int(y)
 if (x < 1000):
  q1 = str(x ** x)[:y]
 else:
  x = Decimal(x)
  q1 = str(int(10 **(x*(x.log10())%1 + y - 1)))
 q2 = str(pow(x, x, 10 ** y)).zfill(y) 
 print(q1 + " " + q2)
