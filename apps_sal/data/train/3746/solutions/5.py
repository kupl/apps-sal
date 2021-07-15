from itertools import count,dropwhile

def next_pal(val): return next(dropwhile(isNotPal, count(val+1)))
def isNotPal(n):   return n!=int(str(n)[::-1])
