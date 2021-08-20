def sum_of_regular_numbers(arr):
    (i, s) = (0, 0)
    while i < len(arr) - 2:
        (n, step) = (1, arr[i] - arr[i + 1])
        while i + 1 + n < len(arr) and arr[i + n] - arr[i + 1 + n] == step:
            n += 1
        if n >= 2:
            s += sum(arr[i:i + n + 1])
        i += n
    return s
