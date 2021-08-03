from math import ceil
def numberOfSteps(s, m): return next((i for i in range(ceil(s / 2), s + 1)if not i % m), -1)
