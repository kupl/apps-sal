def abundant_number(num):
    return sum([e for e in range(1, num) if num % e == 0]) > num
