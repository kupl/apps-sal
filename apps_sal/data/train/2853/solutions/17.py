def solve(lst):
    return sorted(set(lst), key=lst[::-1].index)[::-1]
