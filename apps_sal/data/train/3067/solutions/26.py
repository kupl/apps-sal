getVolumeOfCubiod = lambda *d: (lambda ft, op: ft.reduce(op.mul, d))(__import__('functools'), __import__('operator'))
