def is_sorted_and_how(arr):
    for i in range(len(arr)):
        if sorted(arr) == arr:
            return 'yes, ascending'
        elif sorted(arr, reverse=True) == arr:
            return 'yes, descending'
        else:
            return 'no'
