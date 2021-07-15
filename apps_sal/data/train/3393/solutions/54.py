def list_squared(m, n):
    squares = []
    for i in range(m, n):
        total = sum(get_divisors_sqrd(i))
        if (total ** (1/2)).is_integer():
            squares.append([i, total])
    return squares
            
def get_divisors_sqrd(n):
    divisors = []
    for i in  range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            if i ** 2 not in divisors:
                divisors.append(i ** 2)
            if int(n/i) ** 2 not in divisors:
                divisors.append(int(n / i) ** 2)
    return divisors

