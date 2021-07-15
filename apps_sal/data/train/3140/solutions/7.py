def _sum_squares(number):
    result = 0
    while number > 0:
        carry, digit = number // 10, number % 10
        result += digit * digit
        number = carry
    return result

def _is_happy_number(number):
    seens = set()
    while number > 1:
        # print('number:', number)
        sum_squares = _sum_squares(number)
        # print('sum_squares:', sum_squares)
        if sum_squares in seens:
            return False
        seens.add(sum_squares)
        # print('seens:', seens)
        number = sum_squares
    return True

def happy_numbers(n):
    result = []
    for number in range(1, n + 1):
        if _is_happy_number(number):
            result.append(number)
    return result
