def consecutive(arr):
    return len(range(min(arr), max(arr) + 1)) - len(arr) if arr else 0
