t = int(input())
for _ in range(t):
 a = int(input(),2)
 b = int(input(),2)
 c = 0
 while b!=0:
  u = a^b
  v = a&b
  a = u
  b = 2*v
  c += 1
 print(c)
