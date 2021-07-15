import sys
test_cases = int(input())
for i in range(0,test_cases):
 count = input().split()
 count_r = int(count[0])
 count_g = int(count[1])
 count_b = int(count[2])
 k = int(input())
 if k is 1:
  print(1)
 else:   
  total = 0
  for i in range (1,k):
   if count_r != 0:
    count_r = count_r -1 
    total =total+1 
   if count_g != 0:
    count_g = count_g -1 
    total =total+1 
   if count_b != 0:
    count_b = count_b -1 
    total =total+1 
  total =total + 1
  print(total)

