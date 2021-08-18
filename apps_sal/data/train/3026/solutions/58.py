def min_value(digits):
    storage = []
    for scan in digits:
        if str(scan) not in storage:
            storage.append(str(scan))
    storage.sort()
    return int("".join(storage))
