def groupsInInterval(L,R,M,N):
 if(R<=N):
  return (R - (L-1)) -(R//M - (L-1)//M)
 else:
  return 0
def power(a,b):
 # print(a,'**',b, a**b)
 MOD = 998244353
 res = 1
 while(b>0):
  # print('a = ', a,"b = ",b)

  if(b%2):
   res*=a
   res%=MOD
  b//=2
  a*=a
  a%=MOD
 # print('res',res)
 return res

while(True):
 try:
  test = int(input())
 except EOFError:
  break
 for i in range (test):
  MOD = 998244353
  n,m = list(map(int,input().split()))
  taken,ways = 0,1
  for i in range(1,70):
   # print(ways)
   L = n//m**i + 1;
   R = n//m**(i-1)
   groups = groupsInInterval(L,R,m,n)
   if(i%2==0):
    taken+= (i//2 )*groups
    # print("ways ",ways)
    ways*= power((i//2 +1),groups)
    # ways*= ((i//2 +1)**groups)
   else:
    taken+= ((i+1)//2)*groups
    ways *= (1)
  print(taken,ways%MOD)

