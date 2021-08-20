def array_madness(a, b):
    return sum(map(2.0.__rpow__, a)) > sum(map(3.0.__rpow__, b))
