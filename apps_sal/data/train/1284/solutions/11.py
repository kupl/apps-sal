def func(n, a):
 if a[n//4]==a[n//4-1]:
  return -1
 else:
  x = a[n//4]
 if a[2*n//4]==a[2*n//4-1]:
  return -1
 else:
  y = a[2*n//4]
 if a[3*n//4]==a[3*n//4-1]:
  return -1
 else:
  z = a[3*n//4]
  
 return str(x)+" "+str(y)+" "+str(z)
 
 

for _ in range(int(input())):
 n = int(input())
 a = sorted((map(int, input().split())))
 print(func(n, a))
