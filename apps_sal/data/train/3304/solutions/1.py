def is_inertial(lst):
    odds = [n for n in lst if n % 2 == 1]
    evens = sorted((n for n in lst if n % 2 == 0))[-2:]
    return bool(odds) and max(lst) in evens and (not evens[:-1] or min(odds) > evens[-2])
