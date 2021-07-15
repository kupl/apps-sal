from heapq import nlargest
from functools import reduce
from operator import mul

max_product = lambda lst, k: reduce(mul, nlargest(k, lst))
