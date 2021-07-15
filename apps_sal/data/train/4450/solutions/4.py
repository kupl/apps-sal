def consecutive(arr):
    if len(arr) <= 1:
        return 0
    return (max(arr) - min(arr) + 1) - len(arr)
