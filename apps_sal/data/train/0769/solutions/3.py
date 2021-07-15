for i in range(int(input())):
 a,b = list(map(int, input().split( )))
 lis=[ ]
 if a >= b :
  for i in range(1,a+1):
   if a%i==0 :
    if b%i==0:
     lis.append(i)
 else :
  for i in range(1,b+1):
   if b%i==0 :
    if a%i==0:
     lis.append(i)
 print(lis[-1])

