def last_fib_digit(n):
    last = 0
    tmp = 1
    n = n % 60
    for i in range(n):
        last, tmp = tmp, (last + tmp)
    return last % 10
