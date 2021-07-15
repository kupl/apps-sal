for _ in range(eval(input())):
 n,m = list(map(int,input().split()))
 if n*m==1:
  print("No")
 elif (n*m)%2==0:
  if (n==1 and m!=2) or (m==1 and n!=2):
   print("No")
  else:
   print("Yes")
 else:
  print("No") 
