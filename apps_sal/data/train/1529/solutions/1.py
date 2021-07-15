#cook your recipe
from math import factorial
test_cases = int(input())
for _ in range(test_cases):
   n = int(input())
   sum1 = 0
   final_sum = 0
   num = list(map(int, input().split()))
   rep_time = factorial(n - 1)
   rep_count = dict()
   for i in num:
      if i in rep_count:
         rep_count[i] +=1
      else:
         rep_count[i] =1
   for j in rep_count:
      if rep_count[j] ==1:
         sum1 +=  j * factorial(n - rep_count[j])
      else:
         sum1 +=  j * factorial(n-1)/ factorial(n - rep_count[j])
   
   for k in range(n):
      final_sum += sum1 * (10**k)

   print(int(final_sum))
