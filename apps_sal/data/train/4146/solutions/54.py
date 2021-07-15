def is_sorted_and_how(arr):
    k, c = 0, 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            k += 1
        else:
            c += 1
    if k > 0 or c > 0:
        if k > 0 and c == 0:
            return "yes, ascending"
        elif c > 0 and k == 0:
            return "yes, descending"
    return "no"
