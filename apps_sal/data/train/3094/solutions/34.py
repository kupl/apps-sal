def validation(foo):
    def wrapper(x):
        return foo(x or [0])
    return wrapper

@validation
def sum_array(x):
    return sum(x) - min(x) - max(x) * bool(x[1:])
        

