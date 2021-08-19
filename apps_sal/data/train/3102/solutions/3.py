def locker_run(lockers):
    return [n * n for n in range(1, int(1 + lockers ** 0.5))]
