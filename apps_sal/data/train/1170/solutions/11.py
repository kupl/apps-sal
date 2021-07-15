
for i in range(int(input())):
 n,k=map(int,input().split())
 a=list(map(int,input().split()))
 sum=""
 for i in range(len(a)):
  if(a[i]%k==0):
   sum=sum+"1"
  else:
   sum=sum+"0"
 print(sum)
