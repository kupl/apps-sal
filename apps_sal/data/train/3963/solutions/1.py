def amicable_numbers(n1, n2):
    return spd(n1) == n2 and spd(n2) == n1

def spd(n):
    return sum(i for i in range(1, n) if n % i == 0)
