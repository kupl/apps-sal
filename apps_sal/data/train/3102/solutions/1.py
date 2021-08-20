def locker_run(lockers):
    return [n * n for n in range(1, int(lockers ** 0.5 + 1))]
