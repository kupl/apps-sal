def solve(arr):
    return sorted(set(arr), key=arr[::-1].index)[::-1]
