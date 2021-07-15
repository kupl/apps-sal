from functools import reduce
def sum_mix(arr):
    #your code here
    return reduce((lambda x,y: int(x)+int(y)),arr)
