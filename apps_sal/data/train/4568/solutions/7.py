from operator import mul
from itertools import accumulate

def A(li): return list(accumulate(li, mul))

def find_min_max_product(arr, k):
    if len(arr) < k:return
    
    arr = sorted(arr)[::-1]
    positive = [i for i in arr if i > 0]
    negative = [i for i in arr if i <= 0][::-1]
    neg, pos = A(negative), A(positive) 
    
    maximum = get(pos, neg, A(arr), [], max, k)
    minimum = get(pos, A(negative[::-1]), A(arr[::-1]), neg, min, k)
    
    return (minimum, maximum)

def get(pm, nm, tm, nm1, func, k):
    return func([func([nm[i] * pm[k - i - 2]] + ([nm1[i] * pm[k - i - 2]] if nm1 else [])) for i in range(len(nm)) if  0<=k-i-2<len(pm)]
               +[func(i[k - 1] for i in [pm, nm, tm, nm1] if k - 1 < len(i))])
