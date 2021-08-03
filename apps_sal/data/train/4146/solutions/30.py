def is_sorted_and_how(arr):
    s = 0
    t = 0
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            s += 1
        elif arr[i] > arr[i + 1]:
            t += 1
    if t == len(arr) - 1:
        return "yes, descending"
    elif s == len(arr) - 1:
        return "yes, ascending"
    else:
        return 'no'
