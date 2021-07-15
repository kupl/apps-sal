from functools import reduce
def positive_sum(arr):
    return reduce((lambda acc,n: acc+n if n>0 else acc), arr, 0)

