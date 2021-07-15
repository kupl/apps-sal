def solve(stg, s):
    n = 1
    if stg[s] == "(":
        while n and s < len(stg):
            n, s = n + {"(": 1, ")": -1}.get(stg[s+1], 0), s + 1
    return -1 if n else s

