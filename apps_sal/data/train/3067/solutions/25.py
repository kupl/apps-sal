getVolumeOfCubiod = lambda *d: ((lambda ft, op: ft.reduce(op.mul, d))(*[__import__(q) for q in ['functools', 'operator']]))
