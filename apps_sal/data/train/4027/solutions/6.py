def sum_nested_numbers(x):
    return sum(f(x))

def f(lst, v=1):
    for x in lst:
        if isinstance(x, (list,tuple)):
            for j in f(x, v+1):
                yield j
        else:
            yield x**v
