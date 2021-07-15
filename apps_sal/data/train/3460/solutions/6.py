from math import factorial
from functools import reduce
from operator import mul
uniq_count=lambda a:factorial(len(a))//reduce(mul,[factorial(a.lower().count(i))for i in set(a.lower())],1)
