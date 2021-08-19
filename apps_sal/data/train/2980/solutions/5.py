def divisors(n):
    count = 2
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    return count


def find_min_num(num):
    i = 2
    while True:
        d = divisors(i)
        if d == num:
            return i
        i += 1
