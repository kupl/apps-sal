def array_madness(a, b):
    return sum([num**3 for num in b]) < sum([num**2 for num in a])
