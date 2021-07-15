mod=10**9+7
def pow2(x):
 p,n=1,2
 while(x):
  if(x & 1): p=((p%mod) * (n%mod))%mod

  n=((n%mod) * (n%mod))%mod
  x//=2

 return p

def count_bit(val):
 bit=0
 for i in range(30):
  if(val >> i & 1):bit+=1

 return bit
   
def answer():

 val=b[0]
 po2=0
 for i in range(1,len(b)):
  if(val > b[i]):return 0
  po2+=count_bit(val & b[i])
  val=b[i]

 return pow2(po2)%mod


for T in range(int(input())):
 n=int(input())
 b=list(map(int,input().split()))

 print(answer())
 

