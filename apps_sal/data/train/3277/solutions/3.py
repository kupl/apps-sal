from operator import add as addition, sub as subtraction, mul as multiplication, truediv as division

def calc_type(a, b, res):
    return next(
        name for name in ['addition', 'subtraction', 'multiplication', 'division']
        if globals()[name](a, b) == res
    )
