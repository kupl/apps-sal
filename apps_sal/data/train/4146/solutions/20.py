from operator import le,ge

def is_sorted_and_how(arr):
    if all(map(le,arr,arr[1:])): return 'yes, ascending'
    elif all(map(ge,arr,arr[1:])): return 'yes, descending'
    else: return 'no'
