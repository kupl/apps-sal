import calendar as c
def solve(a, b):
    weeks = [j for i in range(a, b+1) for j in [1,3,5,7,8,10,12] if c.monthrange(i, j) == (4, 31)]
    return (c.month_name[weeks[0]][:3], c.month_name[weeks[-1]][:3], len(weeks))
