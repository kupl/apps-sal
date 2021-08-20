def solve(n):
    print('starting with {0}'.format(n), flush=True)

    def is_prime(p):
        if p % 2 == 0:
            return False
        for x in range(3, int(p ** 0.5)):
            if p % x == 0:
                return False
        return True
    if is_prime(n):
        return n
    step = n % 2 + 1
    while 1:
        if is_prime(n - step):
            return n - step
        elif is_prime(n + step):
            return n + step
        else:
            step += 2
    return None
