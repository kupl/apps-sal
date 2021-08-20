def abundant_number(num):
    return sum((i for i in range(1, num // 2 + 1) if not num % i)) > num
