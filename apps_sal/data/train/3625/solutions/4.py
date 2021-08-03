def sum_of_regular_numbers(arr):
    i = s = 0
    l = len(arr)
    while i < l - 1:
        temp, diff = [], arr[i + 1] - arr[i]
        while i < l - 1 and arr[i + 1] - arr[i] == diff:
            temp.extend([arr[i], arr[i + 1]])
            i += 1
        if len(set(temp)) > 2:
            s += sum(set(temp))
    return s
