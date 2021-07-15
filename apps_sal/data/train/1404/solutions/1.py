import sys
test_cases = int(input())
for i in range(0,test_cases):
 count = input().split()
 #print count
 count_r = int(count[0])
 count_g = int(count[1])
 count_b = int(count[2])
 k = int(input())
 if k is 1:
  total =1
 else:   
  total = 1
  if count_r < k:
   total = total + count_r
  else:
   total = total + (k-1)
  if count_g < k:
   total = total + count_g
  else:
   total = total + (k-1) 
  if count_b < k:
   total = total + count_b
  else:
   total = total + (k-1)
 
 print(total)
