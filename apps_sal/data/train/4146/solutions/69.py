def is_sorted_and_how(arr):
    if arr == sorted(arr):
        answer = 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        answer = 'yes, descending'
    else:
        answer = 'no'
    return answer
