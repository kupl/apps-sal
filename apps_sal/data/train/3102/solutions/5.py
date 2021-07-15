def locker_run(lockers):
    i = 0
    box = [0] * lockers
    while i < lockers:
        for x in range(i, lockers, i + 1):
            box[x] += 1
        i += 1
    return [c + 1 for c in range(len(box)) if box[c] % 2 != 0]
