# cook your dish here
t=int(input())
for cases in range(t):
 n,k=map(int,input().split())
 arr=list(map(int,input().split()))
 s=''
 for i in range(len(arr)):
  if arr[i] % k == 0:
   s=s+ '1'
  else:
   s=s+ '0'
 print(s,end=" ")
 print()
