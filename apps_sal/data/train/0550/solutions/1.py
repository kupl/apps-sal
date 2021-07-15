def bitLen(int_type):
 length = 0
 while (int_type):
  int_type >>= 1
  length += 1
 return(length)
def rot(b):
 b=b[-1]+b[:-1]
 return b
for __ in range(int(input())):
 ans=0
 r=0
 x=0
 c=0
 a, b = map(int, input().split())
 if a>=b:
  r = bitLen(a)
  b=(bitLen(a)-bitLen(b))*'0'+bin(b).replace('0b','')
  a=bin(a).replace('0b','')
 else:
  r = bitLen(b)
  a = (bitLen(b) - bitLen(a)) * '0' + bin(a).replace('0b', '')
  b = bin(b).replace('0b', '')
 for d in range(r):
  x=int(a,2)^int(b,2)
  b=rot(b)
  if ans < x:
   ans=x
   c=d
 print(c,ans)
