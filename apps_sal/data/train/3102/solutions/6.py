def locker_run(lockers):
    # ..
    return [x * x for x in range(1, lockers + 1) if x * x <= lockers]
