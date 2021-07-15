def first_non_consecutive(arr):
    return None if list(range(arr[0], arr[-1] + 1)) == arr else [arr[i + 1] for i in range(0, len(arr) - 1) if arr[i] + 1 != arr[i + 1]][0]
