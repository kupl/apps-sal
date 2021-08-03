def array_madness(a, b):
    sum_a = sum(x**2 for x in a)
    sum_b = sum(x**3 for x in b)
    if sum_a > sum_b:
        return True
    else:
        return False
