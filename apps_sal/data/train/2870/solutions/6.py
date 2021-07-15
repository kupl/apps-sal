from collections import Counter
def same(arr_a, arr_b):
    return Counter(frozenset(x) for x in arr_a) == Counter(frozenset(x) for x in arr_b)
