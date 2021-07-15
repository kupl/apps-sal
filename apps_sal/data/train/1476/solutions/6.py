from collections import Counter
import math
mod = (pow(10,9) + 7)
t = int(input())

for _ in range(t):
 s = input()
 p = 1
 count = dict(Counter(s))
 for i in count:
  p = p * math.factorial(count[i]) 
 x = math.factorial(len(s)) // p
 x = x % mod
 print(x)
