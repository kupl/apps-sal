from functools import reduce
def positive_sum(arr):
    arr = list(filter((lambda x: x > 0), arr))
    try:
        return reduce((lambda x,y: x+y), arr)
    except:
        return 0

