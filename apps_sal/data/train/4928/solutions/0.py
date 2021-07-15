def binRota(arr):
    return [name for i, row in enumerate(arr) for name in row[::-1 if i % 2 else 1]]
