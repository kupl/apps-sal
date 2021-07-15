def XOR(x,y,n):
 c = 0
 for z in range(0,n+1):
  a = x^z
  b = y^z
  if(a < b):
   c+=1
 return c


T = int(input())
for t in range(T):
 x,y,n = map(int,input().split())
 result = XOR(x,y,n)
 print(result)
