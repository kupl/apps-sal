def _sum_squares(num):
    ss = 0
    while num > 0:
        (div, digit) = (num // 10, num % 10)
        ss += digit * digit
        num = div
    return ss


def _is_happy_number(num):
    seens = set()
    while num > 1:
        ss = _sum_squares(num)
        if ss in seens:
            return False
        seens.add(ss)
        num = ss
    return True


def happy_numbers(n):
    result = []
    for num in range(1, n + 1):
        if _is_happy_number(num):
            result.append(num)
    return result
