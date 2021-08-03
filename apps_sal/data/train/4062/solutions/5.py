def solve(arr):
    return [a for i, a in enumerate(arr[:-1]) if a > max(arr[i + 1:])] + [arr[-1]]
