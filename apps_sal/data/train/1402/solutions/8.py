for _ in range(0,int(input())):
 a=input()
 b=input()
 def f(a,b):
  y=0
  while b>0:
   u=a^b
   v=a&b
   a=u
   b=v*2
   y+=1
  return y
 print(f(int(a,2),int(b,2)))

