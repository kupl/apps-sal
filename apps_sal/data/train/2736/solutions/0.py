from functools import cmp_to_key

cmp = lambda a, b: int('%i%i' % (b, a)) - int('%i%i' % (a, b))
largest_arrangement = lambda n: int(''.join(str(i) for i in sorted(n, key = cmp_to_key(cmp))))
