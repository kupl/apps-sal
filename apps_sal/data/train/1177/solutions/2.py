def gcd(x,y):
 if y==0:
  return x
 else :
  return (gcd(y,x%y))
T=input()
T=int(T)
t=1
while t<=T:
 s=input()
 s=s.split()
 t=t+1
 N=int(s[0])
 K=int(s[1])
 if N<K:
  print("0")
  continue
 Kdash=N-K
 if Kdash < K:
  K = Kdash
 num=[]
 denom=[]
 for i in range(1,K+1):
  denom.append(i)
 for i in range(N, N-K , -1):
  num.append(i)
 for i in range(0,K):
  for j in range(0,K):
   if denom[i]>1:
    g=gcd(num[j],denom[i])
    denom[i]=denom[i]/g;
    num[j]=num[j]/g;
   else :
    break
 
 ret=1
 for i in range (0,K):
  ret=ret*num[i]
 print(ret)
