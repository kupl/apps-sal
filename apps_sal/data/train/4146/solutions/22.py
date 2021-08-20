def is_sorted_and_how(arr):
    return all((arr[i] < arr[i + 1] for i in range(len(arr) - 1))) and 'yes, ascending' or (all((arr[i] > arr[i + 1] for i in range(len(arr) - 1))) and 'yes, descending') or 'no'
