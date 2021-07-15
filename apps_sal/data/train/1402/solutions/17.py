t = int(input())
for j in range(t):
 a = int(input(),2)
 b = int(input(),2)
 i = 0
 while b>0:
  u = a^b
  v = a&b
  a = u
  b = 2*v
  i+=1

 print(i)
