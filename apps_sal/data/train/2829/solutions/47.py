def array_madness(a, b):
    sum_of_a = 0
    sum_of_b = 0
    for x in range(len(a)):
        sum_of_a += a[x] ** 2
    for y in range(len(b)):
        sum_of_b += b[y] ** 3
    if sum_of_a > sum_of_b:
        return True
    else:
        return False
