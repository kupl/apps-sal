from functools import reduce; max_product=lambda lst, n: reduce(lambda a,b: a*b, sorted(lst)[-n:],1)
