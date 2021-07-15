t=int(input())
while(t>0):
 t-=1
 nk=list(map(int,input().split()))
 n=int(nk[0])
 k=int(nk[1])
 arr=[0]*10
 while n>0:
  temp = n%10
  n = int(n/10)
  arr[temp] = 1
 count = 0;
 for i in range(10):
  if(arr[i]==1):
   count+=1
 print(count**3);
