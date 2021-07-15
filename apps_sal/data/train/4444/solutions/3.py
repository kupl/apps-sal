def abundant_number(num):
    # O(sqrt(num))
    sum_divisors = 1
    int_sqrt = int(num ** 0.5)
    for div in range(2, int_sqrt + 1):
        if num % div == 0:
            # Add the factor and its complement
            # If num == 12 and div == 2, add 2 and 6
            sum_divisors += div + num // div
    if int_sqrt ** 2 == num: # We count the square root twice if num is a perfect square
        sum_divisors -= int_sqrt
    return sum_divisors > num
