from heapq import nlargest
from functools import cmp_to_key

def oddity(n1, n2):
    while True:
        n1, m1 = divmod(n1, 2)
        n2, m2 = divmod(n2, 2)
        if m1 != m2 or m1 == 0 == m2 or n1 == n2:
            break
    return -1 if m1 < m2 else m1 > m2
    
def oddest(arr):
    res = nlargest(2, arr, key = cmp_to_key(oddity))
    if res and (len(res) == 1 or oddity(res[0], res[1])):
        return res[0]
