# cook your dish here
for _ in range(int(input())):
 
 n = int(input())
 if n==1:
  print('2')
 elif n%2==0:
  print(-1)
 else:
  x=bin(n)[2:].count('0')
  if x==0:
   ans=n//2
   print(ans)
  else:
   print(-1)

