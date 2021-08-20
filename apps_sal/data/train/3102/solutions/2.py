def locker_run(lockers):
    a = [1]
    while len(a) < int(lockers ** 0.5):
        if 1 < lockers < 9 or (len(a) < 2 and lockers >= 9):
            a.append(4)
        else:
            a.append(a[-1] * 2 - a[-2] + 2)
    return a
