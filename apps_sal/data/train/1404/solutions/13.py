import sys
test_cases = int(input())
for i in range(0,test_cases):
 count_r,count_g,count_b = input().split()
 count_r = int(count_r)
 count_g = int(count_g)
 count_b = int(count_b)
 k = int(input())
 if k is 1:
  print(1)
 else:   
  total = 0
  for i in range (1,k):
   if count_r is not 0:
    count_r = count_r -1 
    total =total+1 
   if count_g is not 0:
    count_g = count_g -1 
    total =total+1 
   if count_b is not 0:
    count_b = count_b -1 
    total =total+1 
  total =total + 1
  print(total)

