from collections import Counter

def example_sort(arr, example_arr):
    c = Counter(arr)
    return [n for n in example_arr for _ in range(c[n])]
