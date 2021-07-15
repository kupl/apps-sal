fact = []
fact.append(1)
for i in range(1,100001):
 fact.append((i*fact[i-1])%1000000007)
 
def power(a,b,p):
 x=1
 y=a
 while(b>0):
  if(b%2 == 1):
   x=(x*y)
   if(x>p):
    x=x%p
  y=(y*y)
  if(y>p):
   y=y%p
  b=b/2
 
 return x
 
def inverse(N,p):
 return power(N,p-2,p)
 
def combination(N,R,p):
 return (fact[N]*((inverse(fact[R],p)*inverse(fact[N-R],p))%p))%p
 
T = int(input())
 
for i in range(T):
 N,K = [int(y) for y in input().split()]
 A = [int(arr) for arr in input().split()]
 numZ = 0;
 answer = 0;
 p = 1000000007
 for j in range(len(A)):
  if(A[j] == 0):
   numZ = numZ + 1
 N = N - numZ
 if(numZ > 0):
  if(N > K):
   temp = K;
   while(temp >= 0):
    answer = answer + combination(N,temp,p)
    temp = temp - 1
  else:
   temp = N
   while(temp >= 0):
    answer = answer + combination(N,temp,p)
    temp = temp - 1
 else:
  if(N > K):
   temp = K;
   while(temp >= 0):
    answer = answer + combination(N,temp,p)
    temp = temp - 2
  else:
   temp = N
   while(temp >= 0):
    answer = answer + combination(N,temp,p)
    temp = temp - 2
 print(answer%1000000007)
