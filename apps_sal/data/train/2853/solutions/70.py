from collections import Counter
def solve(arr): 
    return [k for k in Counter(arr[::-1]).keys()][::-1]
