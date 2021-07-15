from math import factorial
from collections import Counter
from functools import reduce
import operator as op

mod = 1000000007



for _ in range(int(input())):    
 s=input()
 c=Counter(s)
 num = factorial(len(s))
 den = 1
 for k in c:
  den*=factorial(c[k])
 print(num//den%mod)

