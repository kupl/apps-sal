def solve(arr):
    return sorted(sorted(arr), key=lambda n: arr.count(n), reverse=True)
