def check_prime_number(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def get_next_prime_number(start, end):
    for number in range(start, end+1):
        if check_prime_number(number) == True:
            return number

def gap(g, m, n):
    prime_number_left = get_next_prime_number(m, n)
    if prime_number_left is None:
        return 
    while True:
        prime_number_right = get_next_prime_number(prime_number_left + 1, n)
        if prime_number_right is None:
            return None
        if prime_number_right - prime_number_left == g:
            return [prime_number_left, prime_number_right]
            
        prime_number_left = prime_number_right
