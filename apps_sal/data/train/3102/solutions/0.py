from math import floor
#Pretty sure this is the fastest implementation; only one square root, and sqrt(n) multiplications.
#Plus, no booleans, because they're super slow.
locker_run = lambda l: [i * i for i in range(1, int(floor(l ** .5)) + 1)]
