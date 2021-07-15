def square_digits(num):
    return int(''.join([str(n * n) for n in map(int, str(num))]))
