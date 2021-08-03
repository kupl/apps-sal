def trotter(n, i=1, digits=set()):
    return n * (i - 1) if len(digits) == 10 else 'INSOMNIA' if i > 900 else trotter(n, i + 1, digits.union(set(str(n * i))))
