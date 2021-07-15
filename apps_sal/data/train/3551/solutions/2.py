def array_previous_less(arr):
    new = [-1]
    for i in range(1, len(arr)):
        curr = arr[i]
        while i and arr[i - 1] >= curr:
            i -= 1
        if i:
            new.append(arr[i - 1])
        else:
            new.append(-1)
    return new
