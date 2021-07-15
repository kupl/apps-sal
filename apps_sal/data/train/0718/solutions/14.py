t = int(input())
while t:
 t = t - 1
 k = int(input())
 if k==1:
  print("0")
 else:
  a = 1
  b = 1
  print("0")
  print("1 1")
  for i in range(2,k):
   for j in range(0,i+1):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
   print()

