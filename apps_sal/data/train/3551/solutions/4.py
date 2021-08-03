def array_previous_less(arr):
    return [next((arr[i - j] for j in range(1, i + 1) if arr[i - j] < v), -1)
            for i, v in enumerate(arr)]
