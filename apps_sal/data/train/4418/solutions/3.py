def get_function(lst):
    (a, b) = (lst[1] - lst[0], lst[0])

    def f(x):
        return a * x + b
    return f if all((f(x) == y for (x, y) in enumerate(lst))) else 'Non-linear sequence'
