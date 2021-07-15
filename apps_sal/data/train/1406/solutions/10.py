Bit= [0] * 256
def initialize(): 
 Bit[0] = 0
 for i in range(256): 
  Bit[i] = (i & 1) + Bit[i // 2] 
def countsetbits(n): 
 return (Bit[n & 0xff] +
   Bit[(n >> 8) & 0xff] +
   Bit[(n >> 16) & 0xff] +
   Bit[n >> 24]) 
initialize()
t=int(input())
for _ in range(t):
 n,q=map(int, input().split())
 a=list(map(int, input().split()))
 e=0
 o=0
 for i in a:
  k=countsetbits(i)
  if (k&1)==0:
   e+=1
  else:
   o+=1
 for j in range(q):
  c=0
  n1=int(input())
  c=countsetbits(n1)
  if c%2==0:
   print(e,o)
  else:
   print(o,e)
