def last_fib_digit(index):
    last, tmp, index = 0, 1, index % 60
    for i in range(index):
        last, tmp = tmp, (last + tmp) % 10
    return last
