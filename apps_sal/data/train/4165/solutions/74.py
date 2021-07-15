from functools import reduce

uni_total=lambda s: reduce(lambda a,b: a+ord(b),s,0)
