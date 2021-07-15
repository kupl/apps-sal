def solve(arr):
    return min(sum(arr) - max(arr), sum(arr) // 2)
