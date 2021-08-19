def amicable_numbers(n1, n2):

    def divisor_sum(x):
        return sum((i for i in range(1, x) if x % i == 0))
    return divisor_sum(n1) == n2 and divisor_sum(n2) == n1
