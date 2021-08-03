def solve(stg):
    return all(abs(abs(ord(x) - ord(y)) - 1) == 1 for x, y in zip(stg, stg[::-1]))
