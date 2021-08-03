def get_function(seq):
    b = seq[0]
    a = seq[1] - b
    def f(x): return a * x + b
    if not all(f(i) == seq[i] for i in range(5)):
        return 'Non-linear sequence'
    return f
