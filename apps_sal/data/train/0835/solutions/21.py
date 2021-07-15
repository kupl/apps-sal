t = input()
t = int(t)
while t:
 n,m = input().split()
 n = int(n)
 m = int(m)
 if (n*m)==2:
  print("Yes")
 elif n==1 or m==1:
  print("No")
 elif n%2 == 0 or m%2 ==0:
  print("Yes")
 else:
  print("No") 
  
 t-=1
