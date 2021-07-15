from collections import Counter

def find_uniq(arr):
    res = Counter(''.join(arr)).most_common()
    return ''.join([x for x in arr if res[-1][0] in x])

