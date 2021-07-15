T=int(input())
for i in range(T):
 S=str(input())
 S=S.split()
 for j in S:
  if j=="not":
   print("Real Fancy")
   break
 else:
  print("regularly fancy")
