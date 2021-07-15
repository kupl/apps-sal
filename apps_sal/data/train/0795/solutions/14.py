# cook your dish here
for _ in range(int(input())):
 n,k,l=map(int,input().split())
 if l*k<n or (n>1 and k==1):
  print("-1")
 else:
  i=1
  for j in range(n):
   if i>k:
    i=1
   print(i,end=" ")
   i+=1
  print("")
