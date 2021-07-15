def factors(num):
    return sum(i for i in range(1, num) if num % i == 0)
def amicable_numbers(n1,n2):
    return factors(n1) == n2 and factors(n2) == n1

