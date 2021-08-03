def check_exam(a, b):
    res = sum(map(lambda x: 0 if x[1] == '' else 4 if x[0] == x[1] else -1, zip(a, b)))
    return 0 if res < 0 else res
