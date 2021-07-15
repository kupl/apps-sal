# cook your dish here
t = int(input())
while t:
 a = int(input())
 d1, d2, max = 1, int(), 0
 mt = a * d1
 mg = 2**d1 - 1
 while mt > mg:
  if mt - mg > max:
   max = mt - mg
   d2 = d1
  d1 = d1 + 1
  mt = a * d1
  mg = 2**d1 - 1
 print(d1 - 1, d2)
 t = t - 1
