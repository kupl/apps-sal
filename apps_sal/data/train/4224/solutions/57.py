def dont_give_me_five(start, end):
    return sum([1 for i in range(min(start, end), max(start, end) + 1) if testFive(i)])


def testFive(num):
    if num < 0:
        num = abs(num)
    while num > 0:
        if num % 10 == 5:
            return False
        num //= 10
    return True
