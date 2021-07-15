def is_sorted_and_how(arr):
    if all(x > y for x,y in zip(arr, arr[1:])):
        return "yes, descending"
    elif all(x < y for x, y in zip(arr, arr[1:])):
        return "yes, ascending"
    else:
        return "no"
