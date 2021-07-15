def solve(array):
    return [*dict.fromkeys(array[::-1]).keys()][::-1]
