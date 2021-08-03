def is_sorted_and_how(arr):
    return ('yes, ascending' if sorted(arr) == arr else 'yes, descending') if (sorted(arr) == arr or sorted(arr, reverse=True) == arr) else 'no'
