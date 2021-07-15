from functools import reduce; min_value=lambda d: reduce(lambda a,b: a*10+b, sorted(set(d)))
