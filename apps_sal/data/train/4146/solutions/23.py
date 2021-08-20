def is_sorted_and_how(arr):
    return {('LT',): 'yes, ascending', ('GT',): 'yes, descending'}.get(tuple(set(map(lambda x, y: 'LT' if x <= y else 'GT', arr, arr[1:]))), 'no')
