def tiaosheng(arr):
    a, b = next(([arr[i - 1], arr[i - 1] + 3 * i] for i, j in enumerate(arr) if j + 3 * i > 60), [arr[-1], arr[-1] + 3 * len(arr)]) if arr else [0, 0]
    return [a, a + 60 - b][b < 60]
