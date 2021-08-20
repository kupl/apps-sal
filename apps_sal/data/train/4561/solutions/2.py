def solve(stg):
    return all((ord(x) - ord(y) in {-2, 0, 2} for (x, y) in zip(stg, stg[::-1])))
