# cook your dish here
for __ in range(int(input())):
 n=int(input())
 arr=list(map(int,input().split()))
 p_c,n_c=0,0
 if n==1:
  if arr[0]>=0:
   print("YES")
  else:
   print("NO")
 else:
  for i in arr:
   if i<0:
    n_c+=i
   else:
    p_c+=i
  
  if p_c>=abs(n_c):
   print("YES")
  else:
   print("NO")

