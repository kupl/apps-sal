from functools import reduce

array_change = lambda arr: reduce(lambda a, u: (max(a[0] + 1, u), a[1] + max(0, a[0] - u + 1)), arr, (-10001, 0))[1]
