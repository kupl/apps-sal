from functools import reduce

billboard=lambda n, p=30: reduce(lambda a,b:a+p, n,0)
