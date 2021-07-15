# cook your dish here
t=int(input())
while t:
 n, k = [int (x) for x in input().split()]
 arr=[int(x) for x in input().split()]
 num=[[0 for i in range(n)] for j in range(n)]
 i=0
 j=0
 count=0
 while i<n:
  while j<n:
   num[i][j]=arr[i]+arr[j]
   j=j+1
  i=i+1 
  j=0
 min =1000000000000000
 i=0
 j=0
 while i<n:
  while j<n:
   if abs(num[i][j]-k)==min and i != j:
    count=count+1
   elif abs(num[i][j]-k)<=min and i !=j:
    min=abs(num[i][j]-k)
    count=1
   j=j+1
  i=i+1
  j=i
 print("{} {}".format(min,count))
 t=t-1
