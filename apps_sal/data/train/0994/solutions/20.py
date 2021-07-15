def main():
 T=int(input())
 for _ in range(T):
  N,X=map(int,input().split())
  A=[0]+list(map(int,input().split()))
  factorsList=[]
  i=1
  ans=0
  while(i*i)<=X:
   if X%i==0:
    factorsList.append(i)
    if i!=(X//i):
     factorsList.append(X//i)
   i+=1
  prefixSums=[0]
  for i in range(1,N+1):
   prefixSums.append(prefixSums[i-1]+A[i])
     
  for factor in factorsList:
   if factor>N:
    continue
   summRequired=X//factor
   d={}
   for i in range(factor,N+1):
    s=prefixSums[i]-prefixSums[i-factor]
    if s<=summRequired:
     if s not in d:
      d[s]=1
     else:
      d[s]+=1
   for i in range(factor,N+1):
    s=prefixSums[i]-prefixSums[i-factor]
    if s<=summRequired:
     if (summRequired-s) in d:
      ans+=d[summRequired-s]
  print(ans)
def __starting_point():
 main()
__starting_point()
