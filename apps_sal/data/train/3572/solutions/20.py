from collections import Counter
def invite_more_women(arr):
    c = Counter(arr)
    return c[1]>c[-1]
