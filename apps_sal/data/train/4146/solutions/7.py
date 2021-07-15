def is_sorted_and_how(arr):
    op, txt = ((int.__le__, 'yes, ascending'), (int.__ge__, 'yes, descending'))[arr[0] > arr[-1]]
    return all(map(op, arr, arr[1:])) and txt or 'no'
