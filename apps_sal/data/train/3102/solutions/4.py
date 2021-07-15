def locker_run(lockers):
    return [i for i in range(1, lockers + 1) if i ** 0.5 % 1 == 0]
