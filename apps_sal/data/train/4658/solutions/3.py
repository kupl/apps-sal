from functools import reduce
from operator import mul

max_product = lambda lst, k: reduce(mul, sorted(lst)[-k:])

