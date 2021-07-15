from functools import reduce
def solve(arr):
    f = lambda x, y: [i*j for i in x for j in y]
    return max(reduce(f, arr))
    
    

