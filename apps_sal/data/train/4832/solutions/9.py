from itertools import islice
def all_non_consecutive(arr):
    return [{'i': c, 'n':b} for c, (a, b) in enumerate(zip(arr, islice(arr, 1, None)), 1) if a + 1 != b]
