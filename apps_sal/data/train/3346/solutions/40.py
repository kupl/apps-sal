import math


def is_prime(num):
    max_num_to_check = int(math.sqrt(num)) + 1
    for number in range(2, max_num_to_check):
        if num % number == 0 and num != number:
            return False
    return True


def gap(g, m, n):
    first_num = -1
    sec_num = -1
    for num in range(m, n):
        if first_num == -1 and is_prime(num):
            first_num = num
            continue
        if sec_num == -1 and is_prime(num):
            sec_num = num
            if sec_num - first_num == g:
                return [first_num, sec_num]
            else:
                sec_num = -1
                first_num = num
    return None
