t = int(input())
for _ in range(t):
 n = int(input())
 if n%2==0:
  for i in range(n):
   for j in range(n):
    if i%2==0:
     if i+j <= (n-1):
      print(n-i-j,end='')
    else:
     if i+j <= (n-1):
      print(j+1,end='')
   print()
 else:
  for i in range(n):
   for j in range(n):
    if i%2==0:
     if i+j <= (n-1):
      print(j+1,end='')
    else:
     if i+j <= (n-1):
      print(n-i-j,end='')
   print()
     

