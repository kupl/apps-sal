def divisors(n):
    return len([l_div for l_div in range(1, n + 1) if n % l_div == 0])
