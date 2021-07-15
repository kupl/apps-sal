from collections import Counter
from math import inf

def oddest(arr):
    c = Counter(map(oddness, arr))
    return max(arr, key=oddness) if c and c[max(c)] == 1 else None
    
def oddness(n):
    if n == -1:
        return inf
    m, is_odd = divmod(n, 2)
    cnt = 0
    while is_odd:
        m, is_odd = divmod(m, 2)
        cnt += 1
    return cnt
