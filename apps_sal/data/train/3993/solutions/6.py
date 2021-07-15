def solve(a):
    return sum(1 if x % 2 == 0 else -1 for x in a if type(x)==int)
