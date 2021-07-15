from datetime import datetime

def solve(arr):
    dts = [datetime(2000, 1, 1, *map(int, x.split(':'))) for x in sorted(arr)]
    delta = max(int((b - a).total_seconds() - 60) for a, b in zip(dts, dts[1:] + [dts[0].replace(day=2)]))
    return '{:02}:{:02}'.format(*divmod(delta//60, 60))
