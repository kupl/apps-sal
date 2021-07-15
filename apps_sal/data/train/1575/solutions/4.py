for t in range(int(input())):
 m=int(input())
 n=int(input())
 o=int(input())
 if m==1 and (n==1 and o==1):
  print(0)
 else:
  print((m+n+o-6)*4)
