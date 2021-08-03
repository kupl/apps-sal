def divisors(n):
    result = [i for i in range(2, n) if n % i == 0]
    return result if result else str(n) + ' is prime'
