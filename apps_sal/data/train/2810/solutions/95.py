def solve(arr):
    return [sum(1 for i, x in enumerate(y.lower()) if ord(x) - 96 == i + 1) for y in arr]
