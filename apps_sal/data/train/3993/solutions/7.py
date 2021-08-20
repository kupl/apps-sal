def solve(a):
    return len([i for i in a if type(i) == int and (not i % 2)]) - len([i for i in a if type(i) == int and i % 2])
