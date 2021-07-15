def solve(array):
    return sorted(sorted(array), key=array.count, reverse=True)
