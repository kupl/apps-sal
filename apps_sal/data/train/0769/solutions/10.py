for i in range(int(input())):
 a,b = input().split()
 a = int(a)
 b = int(b)
 
 if a>b:
  a,b = b,a

 r = 1
 for e in range(1, a+1):
  if a % e == 0 and b % e == 0:
   r = e
 print(r)
