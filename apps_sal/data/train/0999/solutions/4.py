for _ in range(int(input())):
 n = int(input())
 for i in range(1,n+1+1):
  if i%2 == 0:
   for j in range(1,n-i+2):
    print(end=" ")
   num = 65
   for k in range(1,n-(n-i)):
    print(chr(num),end="")
    num += 1
   print("")
  else:
   for j in range(1,n-i+2):
    print(end=" ")
   for k in range(1,n-(n-i)):
    print(k,end="")
   print("")
