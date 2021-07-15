# cook your dish here
t=int(input())
arr=[0,1]
for i in range(2,101):
 arr.append(arr[i-1]+arr[i-2])
while t>0:
 n=int(input())
 m=0
 for i in range(0,n):
  for j in range(0,i+1):
   print(arr[m],end=' ')
   m+=1
  print()
 t-=1
 
 

