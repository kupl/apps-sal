def solve(n):
    if n<=10:
        return [0,4,10,20,35,56,83,116,155,198,244][n]
    else:
        return 292+49*(n-11)
