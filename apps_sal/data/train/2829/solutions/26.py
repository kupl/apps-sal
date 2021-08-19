def array_madness(a, b):
    for i in range(len(a)):
        a[i] = a[i] ** 2
    sum_a = sum(a)
    for i in range(len(b)):
        b[i] = b[i] ** 3
    sum_b = sum(b)
    if sum_a > sum_b:
        return True
    else:
        return False
