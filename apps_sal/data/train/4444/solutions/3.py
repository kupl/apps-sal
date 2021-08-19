def abundant_number(num):
    sum_divisors = 1
    int_sqrt = int(num ** 0.5)
    for div in range(2, int_sqrt + 1):
        if num % div == 0:
            sum_divisors += div + num // div
    if int_sqrt ** 2 == num:
        sum_divisors -= int_sqrt
    return sum_divisors > num
