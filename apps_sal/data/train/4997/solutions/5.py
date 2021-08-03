import math


def find_sum_of_divisors(number):
    not_divisible = []
    sum = 1 + number
    for div in xrange(2, int(round(math.sqrt(number) + 1))):
        if number % div == 0:
            sum += div + number / div
    return sum


def equal_sigma1(nMax):
    checked_numbers = set()
    found_sum = 0
    for num in xrange(528, nMax + 1):
        if num in checked_numbers:
            continue

        number = str(num)
        rev_number = number[::-1]
        rev_num = int(rev_number)

        checked_numbers.add(num)
        checked_numbers.add(rev_num)

        if number == rev_number:
            continue

        if find_sum_of_divisors(num) == find_sum_of_divisors(rev_num):
            found_sum += num + (rev_num if rev_num <= nMax else 0)

    return found_sum  # sum of found numbers
