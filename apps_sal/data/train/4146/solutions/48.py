def is_sorted_and_how(arr):
    c = 0
    a = 0
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            c += 1
            if c == len(arr) - 1:
                return 'yes, ascending'
        elif arr[i] >= arr[i + 1]:
            a += 1
            if a == len(arr) - 1:
                return 'yes, descending'
    else:
        return 'no'
