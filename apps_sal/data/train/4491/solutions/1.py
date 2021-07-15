def solve(a,b):
    return "".join([c for c in a if not c in b]+[c for c in b if not c in a])
