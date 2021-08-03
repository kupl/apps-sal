def split_exp(n): return (lambda d: [('.' + '0' * (i - d - 1) + x, x + '0' * (d - i - 1))[d > i]for i, x in enumerate(n)if x not in '.0'])((len(n), n.find('.'))['.' in n])
