def minimumchanges():
 n = int(input().strip())
 for i in range(0,n):
  N,M = list(map(int, input().strip().split(' ')))
  if((N == 1 and M == 2) or (N == 2 and M == 1)):
   print("Yes")
  elif N == 1 or M == 1:
   print("No")
  elif N%2 == 0 or M%2 == 0:
   print("Yes")
  else:
   print("No")
   


minimumchanges()
