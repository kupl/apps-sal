no_of_testcases = int(input())
for nt in range(no_of_testcases):
 num = int(input()) 
 if num%2 == 0:
  c = num/2
  if c%2==0:
   print("YES")
  else:
   print("NO")
 else:
  print("NO")

