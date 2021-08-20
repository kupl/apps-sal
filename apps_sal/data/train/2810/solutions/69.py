def solve(arr):
    return [sum((ord(c.lower()) - 96 == i + 1 for (i, c) in enumerate(m))) for m in arr]
