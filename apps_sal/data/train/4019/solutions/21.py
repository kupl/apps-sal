def max_multiple(divisor, bound):
    return max(n for n in range(divisor, bound + 1) if n % divisor == 0 and n <= bound and n >=0) if divisor <= bound else 0
