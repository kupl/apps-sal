#

for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 arr = list(map(int,input().split()))
 s=set(arr)
 t1=len(s)
 max=-1
 for i in range(n-k+1):
  temp=set(arr[i:i+k])
  #print(temp,i,k+i+1)
  t=len(temp)
  if t1 == t:
   if max<sum(arr[i:k+i]):
    max=sum(arr[i:k+i])
 print(max)

