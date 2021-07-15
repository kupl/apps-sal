def pre_fizz(n):
    fizz = []
    while n >= 1:
        if n != 0:
            fizz.append(n)
            n = n - 1
            sort_fizz = sorted(fizz)
    return sort_fizz
