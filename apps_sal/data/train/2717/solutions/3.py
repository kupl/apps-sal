def scf(lst):
    for k in range(2, min(lst, default=1) + 1):
        if all((n % k == 0 for n in lst)):
            return k
    return 1
