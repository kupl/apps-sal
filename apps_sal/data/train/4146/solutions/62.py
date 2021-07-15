def is_sorted_and_how(arr):
    # your code here
    if arr[0] == min(arr) and arr[-1] == max(arr):
        return 'yes, ascending'
    elif arr[0] == max(arr) and arr[-1] == min(arr):
        return 'yes, descending'
    else:
        return 'no'
