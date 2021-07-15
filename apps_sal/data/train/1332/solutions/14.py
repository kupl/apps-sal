import sys
 
for q in range(int(sys.stdin.readline())):
 n1,n2 = list(map(int,sys.stdin.readline().split()))
 count = 0
 while n1!=n2:
  while n1>n2:
   n1/=2
   count+=1
  while n2>n1:
   n2/=2
   count+=1
 print(count)

