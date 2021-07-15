
def bint(var):
 decimale = 0
 l = len(var)
 for i in range(l):
  decimale += int(var[i])*(2**(l-i-1))
 return decimale
 
 
t = int(input())
for _ in range(t):
 a, b = map(int, input().split())
 a = bin(a)[2:]
 b = bin(b)[2:]
 if(len(a) > len(b)):
  b = "0"*(len(a)-len(b)) + b
 elif(len(b) > len(a)):
  a = "0"*(len(b)-len(a)) + a
 l = len(a)
 res =0
 val = bint(a)^bint(b)
 temp = b[-1] + b[:l-1]
 x = 1
 while(x < l):
  if(bint(a)^bint(temp) > val):
   val = bint(a)^bint(temp)
   res = x
  temp = temp[-1] + temp[:l-1]
  x += 1
 print(res, val)
