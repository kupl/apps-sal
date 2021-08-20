(m, hollow_triangle) = (lambda s: s[:0:-1] + s, lambda n: [m('_' * i + '#' + '_' * (n - i - 1)) for i in range(n - 1)] + [m(n * '#')])
