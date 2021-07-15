multiply = lambda *a : ( (lambda ft, op: ft.reduce(op.mul, a)) (*[__import__(x) for x in ['functools', 'operator']]))
