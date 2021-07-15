from itertools import combinations as comb

def find_zero_sum_groups(arr, n):
    if not arr: return "No elements to combine"
    
    arr = list(set(arr))
    result = sorted(sorted(x) for x in set(comb(arr, n)) if sum(x) == 0)
    result = sorted(list(x) for x in set(map(tuple, result)))
    
    if not result: return "No combinations"
    
    return result[0] if len(result) == 1 else result

