''' CHFNSWAP - CodeChef SEPT20B'''
import math

def sum_naturals(num):
 return ((num + 1) * num ) / 2


def find_nice_swaps():
 sum_n = sum_naturals((n))
 if sum_n % 2 != 0:
  return 0
 x = (math.sqrt(4*sum_n + 1) - 1) / 2

 left = 0
 right = 0
 if x == int(x):
  if x >= 2:
   left = math.factorial(x) // (2 * math.factorial(x - 2))
  if n - x >= 2:
   right = math.factorial(n-x) // (2 * math.factorial(n-x-2))

 return n - int(x) + left + right
  
 
testcases = int(input())

while testcases > 0:
 n = int(input())
 print(find_nice_swaps())
 testcases -= 1
