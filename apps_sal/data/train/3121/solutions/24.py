def solve(arr):
    rev = set(-x for x in arr)
    return [x for x in arr if abs(x) not in set(arr) or x not in rev][0]
