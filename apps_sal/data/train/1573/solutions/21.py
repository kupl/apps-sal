# cook your dish here
for t in range(int(input())):
 n=int(input())
 if(n%2==0):
  print("NO")
 else:
  print("YES")
  n1=n//2
  for i in range(n):
   s=['0']*n
   c=0
   for j in range(i+1,n):
    s[j]='1'
    c+=1 
    if(c==n1):
     break
   if(c<n1):
    for j in range(n1-c):
     s[j]='1'
   k=''.join(s)
   print(k)
   

