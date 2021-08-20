def triangle(n):
    return int(n * (n + 1) / 2)


def sum_triangular_numbers(n):
    sum = 0
    for i in range(n + 1):
        sum += triangle(i)
    return sum
