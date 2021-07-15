t = int(input())
for _ in range(t):
 ans= -1
 n,l,k = input().split()
 n = int(n)
 l = int(l)
 k = int(k)
 if (k*l >= n) and (l!=1 or n==1)  :
  i=1
  j=1
  while i <= n:
   if j <= l:
    print(j, end=" ")
   else: 
    j=1
    print(j,end=" ")
   j = j+1
   i = i+1
 else:
  print(ans,end="")
 print()
    
