def solve(n, f='0', g='01'):
    return solve(n - 1, g, g + f) if n else f
