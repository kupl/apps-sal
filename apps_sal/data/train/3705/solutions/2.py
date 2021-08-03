heron = lambda*args: (lambda a, b, c, s: round((s * (s - a) * (s - b) * (s - c))**.5, 2))(*args, sum(args) / 2)
