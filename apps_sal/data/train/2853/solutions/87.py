def solve(arr):
    return sorted(set(arr[::-1]), key=arr[::-1].index)[::-1]
